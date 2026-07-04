ENTITY i2c_controller_v2 IS
    PORT (
        -- Global Physical Inputs
        clk             : IN    STD_LOGIC;  -- Internal UFM Oscillator (~4 MHz)
        rst_n           : IN    STD_LOGIC;  -- Top-level Asynchronous Reset
       
        -- Physical I2C Bus Hardware Pins (To Main System Master)
        SCL             : INOUT STD_LOGIC;  -- Serial Clock Line
        SDA             : INOUT STD_LOGIC;  -- Serial Data Line
       
        -- External Address Configuration Pins
        i2c_addr_pins   : IN    STD_LOGIC_VECTOR(6 DOWNTO 0); -- 7 physical address strapping pins
       
        -- Physical Closed-Loop Sensor Inputs
        hall_home_n     : IN    STD_LOGIC;  -- Active-Low Resting Sensor
        hall_travel_n   : IN    STD_LOGIC;  -- Active-Low Full Extension Sensor
       
        -- Physical Actuator Output Drive
        solenoid_gate   : OUT   STD_LOGIC;  -- Output to external 555-PWM circuit
       
        -- Physical Bus Interface to External Parallel Flash IC (Full Read/Write Support)
        flash_addr      : OUT   STD_LOGIC_VECTOR(16 DOWNTO 0); -- 17-bit Address Bus
        flash_data      : INOUT STD_LOGIC_VECTOR(7 DOWNTO 0);  -- Bi-directional 8-bit Data Bus
        flash_ce_n      : OUT   STD_LOGIC;                     -- Chip Enable (Active Low)
        flash_oe_n      : OUT   STD_LOGIC;                     -- Output Enable (Active Low)
        flash_we_n      : OUT   STD_LOGIC                      -- Write Enable (Active Low)
    );
END i2c_controller_v2;

ARCHITECTURE Structural OF i2c_controller_v2 IS
    -- State Machine Enumeration for Process 1 (I2C Controller)
    TYPE t_i2c_state IS (IDLE, RX_ID, CHECK_ID, RX_BYTE, ACK_PHASE, CLK_STRETCH, TX_BYTE, WAIT_STOP);
    SIGNAL i2c_state : t_i2c_state := IDLE;

    -- Inter-Process Internal Handshake Signals (Bridge Wire Flags)
    SIGNAL byte_ready       : STD_LOGIC := '0';
    SIGNAL byte_ack         : STD_LOGIC := '0';
    SIGNAL data_holding_reg : STD_LOGIC_VECTOR(7 DOWNTO 0) := (OTHERS => '0');
    SIGNAL tx_data_buffer   : STD_LOGIC_VECTOR(7 DOWNTO 0) := (OTHERS => '0');

    -- Oversampling Shift Pipes (History Registers)
    SIGNAL scl_pipe : STD_LOGIC_VECTOR(1 DOWNTO 0) := "11";
    SIGNAL sda_pipe : STD_LOGIC_VECTOR(1 DOWNTO 0) := "11";

    -- Synchronous Edge Detection Strobes
    SIGNAL scl_rising       : STD_LOGIC;
    SIGNAL scl_falling      : STD_LOGIC;
    SIGNAL sda_rising       : STD_LOGIC;
    SIGNAL sda_falling      : STD_LOGIC;

    -- Asynchronous Protocol Condition Flags
    SIGNAL start_condition  : STD_LOGIC;
    SIGNAL stop_condition   : STD_LOGIC;

    -- Internal I2C Counters & Core Shift Registers
    SIGNAL bit_counter      : INTEGER RANGE 0 TO 8 := 0;
    SIGNAL rx_shift_reg     : STD_LOGIC_VECTOR(7 DOWNTO 0) := (OTHERS => '0');
    SIGNAL tx_shift_reg     : STD_LOGIC_VECTOR(7 DOWNTO 0) := (OTHERS => '0');
   
    -- Internal Tri-state Control Drivers
    SIGNAL sda_drive_low    : STD_LOGIC := '0';
    SIGNAL scl_clamp_low    : STD_LOGIC := '0';
   
    -- Parallel Flash Data Bus Internal Drivers
    SIGNAL flash_data_out   : STD_LOGIC_VECTOR(7 DOWNTO 0) := (OTHERS => '0');
    SIGNAL flash_write_active : STD_LOGIC := '0';

BEGIN

    -------------------------------------------------------------------
    -- BLOCK A & B: OVERSAMPLING & BUS CONDITION MONITORS
    -------------------------------------------------------------------
    process_oversample : PROCESS(clk)
    BEGIN
        IF rising_edge(clk) THEN
            scl_pipe <= scl_pipe(0) & SCL;
            sda_pipe <= sda_pipe(0) & SDA;
        END IF;
    END PROCESS process_oversample;

    -- Edge Evaluation
    scl_rising  <= '1' WHEN (scl_pipe = "01") ELSE '0';
    scl_falling <= '1' WHEN (scl_pipe = "10") ELSE '0';
    sda_rising  <= '1' WHEN (sda_pipe = "01") ELSE '0';
    sda_falling <= '1' WHEN (sda_pipe = "10") ELSE '0';

    -- Target Evaluates status on SCL line via pipe(0)
    start_condition <= '1' WHEN (sda_falling = '1' AND scl_pipe(0) = '1') ELSE '0';
    stop_condition  <= '1' WHEN (sda_rising = '1' AND scl_pipe(0) = '1') ELSE '0';

    -------------------------------------------------------------------
    -- BLOCK C: PROCESS 1 (I2C CORE) WITH TOP-LEVEL ASYNC RESET
    -------------------------------------------------------------------
    process_i2c_core : PROCESS(clk, rst_n)
    BEGIN
        -- Asynchronous master reset as top-level trigger statement
        IF rst_n = '0' THEN
            i2c_state        <= IDLE;
            bit_counter      <= 0;
            byte_ready       <= '0';
            sda_drive_low    <= '0';
            scl_clamp_low    <= '0';
            data_holding_reg <= (OTHERS => '0');
            tx_shift_reg     <= (OTHERS => '0');
            rx_shift_reg     <= (OTHERS => '0');
           
        ELSIF rising_edge(clk) THEN
           
            -- Stop condition is the ONLY event allowed to exit directly to IDLE
            IF stop_condition = '1' THEN
                i2c_state     <= IDLE;
               
            ELSIF start_condition = '1' THEN
                i2c_state     <= RX_ID; -- Capture incoming target identifier
                bit_counter   <= 0;
                byte_ready    <= '0';
                sda_drive_low <= '0';
                scl_clamp_low <= '0';
               
            ELSE
                CASE i2c_state IS
                   
                    WHEN IDLE =>
								-- do nothing

                    WHEN RX_ID =>
                        IF scl_rising = '1' THEN
                            rx_shift_reg(7 - bit_counter) <= sda_pipe(0);
                            IF bit_counter = 7 THEN
                                i2c_state <= CHECK_ID;
                            ELSE
                                bit_counter <= bit_counter + 1;
                            END IF;
                        END IF;

                    WHEN CHECK_ID =>
                        -- Match against the live physical address pin states
                        IF rx_shift_reg(7 DOWNTO 1) = i2c_addr_pins THEN
                            i2c_state <= ACK_PHASE;
                        ELSE
                            -- Mismatched identification routes to passive isolation state
                            i2c_state <= PREP_STOP;
                        END IF;

                    WHEN ACK_PHASE => -- still fucking wrong???
                        IF scl_falling = '1' THEN
                            sda_drive_low    <= '1'; -- Drive physical pin low to ACK
                            data_holding_reg <= rx_shift_reg;
                            byte_ready       <= '1';
                           
                            IF byte_ack = '1' THEN
                                i2c_state <= CLK_STRETCH;
                            ELSE
                                bit_counter <= 0;
                                -- Assess operational path (Read/Write bit verification)
                                IF rx_shift_reg(0) = '1' THEN
                                    tx_shift_reg <= tx_data_buffer;
                                    i2c_state    <= TX_BYTE;
                                ELSE
                                    i2c_state    <= RX_BYTE;
                                END IF;
                            END IF;
								ELSIF scl_rising = '1' and byte_ack = '0' THEN
                            byte_ready    <= '1';
									 sda_drive_low <= '0';
                        END IF;

                    WHEN RX_BYTE =>
                        IF scl_rising = '1' THEN
                            rx_shift_reg(7 - bit_counter) <= sda_pipe(0);
                            IF bit_counter = 7 THEN
                                i2c_state <= ACK_PHASE;
                            ELSE
                                bit_counter <= bit_counter + 1;
                            END IF;
                        END IF;

                    WHEN TX_BYTE => -- what the hell is this doing???
                        IF tx_shift_reg(7) = '0' THEN
                            sda_drive_low <= '1';
                        ELSE
                            sda_drive_low <= '0';
                        END IF;

                        IF scl_falling = '1' THEN
                            tx_shift_reg <= tx_shift_reg(6 DOWNTO 0) & '1';
                            IF bit_counter = 7 THEN
                                sda_drive_low <= '0';
                                i2c_state     <= PREP_STOP; -- Isolate boundary path
                            ELSE
                                bit_counter <= bit_counter + 1;
                            END IF;
                        END IF;

                    WHEN CLK_STRETCH =>
                        scl_clamp_low <= '1'; -- Lock SCL low via hardware stretch
                        byte_ready    <= '0';
                       
                        IF byte_ack = '0' THEN
                            scl_clamp_low <= '0'; -- Release the clock line lock
                            bit_counter   <= 0;
                           
                            IF rx_shift_reg(0) = '1' THEN
                                tx_shift_reg <= tx_data_buffer;
                                i2c_state    <= TX_BYTE;
                            ELSE
                                i2c_state    <= RX_BYTE;
                            END IF;
                        END IF;

						  WHEN PREP_STOP =>
								i2c_state	  <= WAIT_STOP;
								-- Absorb unmapped transactions safely until explicit STOP pulse arrives
                        bit_counter   <= 0;
								byte_ready    <= '0';
								sda_drive_low <= '0';
								scl_clamp_low <= '0';

                    WHEN WAIT_STOP =>
								-- do nothing

                    WHEN OTHERS =>
                        i2c_state <= IDLE;
                END CASE;
            END IF;
        END IF;
    END PROCESS process_i2c_core;

    -------------------------------------------------------------------
    -- BLOCK D: PHYSICAL TRI-STATE PIN DRIVER LOGIC
    -------------------------------------------------------------------
    -- Electrical Compliance Driver Blocks for Open-Drain Environments
    SDA <= '0' WHEN (sda_drive_low = '1') ELSE 'Z';
    SCL <= '0' WHEN (scl_clamp_low = '1') ELSE 'Z';

    -- Bi-Directional Parallel Flash Bus Output Driver
    flash_data <= flash_data_out WHEN (flash_write_active = '1') ELSE (OTHERS => 'Z');

END ARCHITECTURE Structural;
