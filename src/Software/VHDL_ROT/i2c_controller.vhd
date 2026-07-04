library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity i2c_controller is
    Port (
        clk               : in    std_logic;
        rst_n             : in    std_logic;
		  
		  i2c_addr          : in    std_logic_vector(6 downto 0);
		  sda               : inout std_logic;
        scl               : in    std_logic;
        
		  token_flag        : inout std_logic;
        shared_data       : inout std_logic_vector(7 downto 0);

        -- Solenoid System Pins Passed Out from Sub-Module Hierarchy
        homing_switch     : in    std_logic;
        step_fwd          : out   std_logic;
        step_rev          : out   std_logic;

        -- Priority Flash Controller Links Leading into Master Core Multiplexer
        flash_request_out : out   std_logic;
        flash_addr_out    : out   std_logic_vector(16 downto 0);
        flash_req_pulse   : out   std_logic;
        flash_system_bsy  : in    std_logic
    );
end i2c_controller;

architecture Behavioral of i2c_controller is
    type i2c_state_t is (ST_IDLE, ST_START, ST_CHCK_ADDR, ST_GET_CMD, ST_RX_DATA, ST_SEND_ACK, ST_LAUNCH_ACT, ST_STOP);
    signal current_state : i2c_state_t := ST_IDLE;

    signal scl_sync : std_logic_vector(1 downto 0) := "11";
    signal sda_sync : std_logic_vector(1 downto 0) := "11";
	 signal scl_falling_edge	: std_logic;
	 signal scl_rising_edge		: std_logic;
	 signal sda_falling_edge	: std_logic;
	 signal sda_rising_edge		: std_logic;

    signal sda_out_en : std_logic := '0';
    signal sda_out    : std_logic := '1';

    -- Sub-Module Instantiation Wires
    signal wire_start_act   : std_logic := '0';
    signal wire_target_pos  : unsigned(5 downto 0) := (others => '0');
    signal wire_current_pos : unsigned(5 downto 0);
    signal wire_act_busy    : std_logic;
begin
	sda <= sda_out when (sda_out_en = '1') else 'Z';
	
	start_detect <= '1' when (scl_sync(0) = '1' and sda_sync = "10") else '0';
	stop_detect <= '1' when (scl_sync(0) = '1' and sda_sync = "01") else '0';
	
	scl_falling_edge <= '1' when (scl_sync = "10") else '0';
	scl_rising_edge <= '1' when (scl_sync = "01") else '0';
	
	
	U_ACTUATOR : entity work.actuation_controller
	port map (
		clk					=> clk,
		rst_n             => rst_n,

		start_actuation   => wire_start_act,
		target_pos        => wire_target_pos,
		current_pos       => wire_current_pos,
		actuation_busy    => wire_act_busy,

		-- Cascaded Memory Lanes: Routed straight up to top-level multiplexer wires
		flash_req_addr    => flash_addr_out,
		flash_rx_data     => (others => '0'),
		flash_execute     => flash_req_pulse,
		flash_system_bsy  => flash_system_bsy,

		-- Distinct Solenoid Track Connections
		homing_switch_pin => homing_switch,
		step_fwd_pin      => step_fwd,
		step_rev_pin      => step_rev
	);

    -------------------------------------------------------------------
    -- SERIAL SHIFT INTERFACE PARSING CONTROLLER
    -------------------------------------------------------------------
    process(clk, rst_n)
        variable bit_counter  : integer range 0 to 7 := 7;
        variable rx_shift_reg : std_logic_vector(7 downto 0) := (others => '0');
        variable command_byte : std_logic_vector(7 downto 0) := (others => '0');
    begin
        if rst_n = '0' then
            current_state     <= ST_IDLE;
            sda_out_en        <= '0';
            flash_request_out <= '0';
            wire_start_act    <= '0';
            wire_target_pos   <= (others => '0');
        elsif rising_edge(clk) then
            scl_sync <= (scl_sync(0) & scl);
            sda_sync <= (sda_sync(0) & sda);

            wire_start_act <= '0'; -- Standard clock cycle fallback strobe

            if scl_falling_edge = '1' then
                case current_state is
                    when ST_IDLE =>
								if start_detect = '1' then
									current_state <= ST_START;
								end if;
						  when ST_START =>
                        if token_flag = '1' then
                            bit_counter := 7;
                            current_state <= ST_CHCK_ADDR;
                        end if;
                    when ST_CHCK_ADDR =>
                        rx_shift_reg(bit_counter) := sda_sync(0);
                        if bit_counter > 0 then
									bit_counter := bit_counter - 1;
                        else
									current_state <= ST_SEND_ACK;
								end if;
                    when ST_SEND_ACK =>
                        if rx_shift_reg(7 downto 1) = i2c_addr then
									-- ACK
									sda_out_en <= '1';
									sda_out <= '0';
									if scl_falling = '1' then
										current_state <= ST_GET_CMD;
									end if;
								else
									-- NACK
									sda_out_en <= '0';
									sda_out <= '1';
									if scl_falling = '1' then
										current_state <= ST_STOP;
									end if;
								end if;
								bit_counter := 7;
                    when ST_GET_CMD =>
                        -- Release ACK
								sda_out_en <= '0';
								sda_out <= '1';
								
                        rx_shift_reg(bit_counter) := sda_sync(0);
                        if bit_counter > 0 then 
									bit_counter := bit_counter - 1;
                        else
									command_byte := rx_shift_reg;
									current_state <= ST_RX_DATA;
									bit_counter := 7;
								end if;
                    when ST_RX_DATA =>
                        rx_shift_reg(bit_counter) := sda_sync(0);
                        if bit_counter > 0 then
									bit_counter := bit_counter - 1;
                        else
                            shared_data <= rx_shift_reg;
                            -- Check if message demands active solenoid movement
                            if command_byte = x"A1" or command_byte = x"B2" then -- Encoding/SetPos Codes
                                wire_target_pos <= unsigned(rx_shift_reg(5 downto 0)); -- how is this known here for encoding??? that should just perform a single step;
                                wire_start_act  <= '1'; -- Drive inner actuator trigger pulse high
                                current_state   <= ST_LAUNCH_ACT;
                            else
                                token_flag <= '0'; -- Static math lookup command, hand pass over
                                current_state <= ST_STOP;
                            end if;
                        end if;
                    when ST_LAUNCH_ACT =>
                        if wire_act_busy = '0' then
                            token_flag <= '0'; -- Solenoid action completely finished, safe to pass control
                            current_state <= ST_STOP;
                        end if;
						  when ST_STOP =>
								if stop_detect = '1' then
									current_state <= ST_IDLE;
								end if;
                    when others =>
								current_state <= ST_IDLE;
                end case;
            end if;
        end if;
    end process;
end Behavioral;