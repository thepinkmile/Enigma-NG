library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity actuation_controller is
    Port (
        clk               : in    std_logic;
        rst_n             : in    std_logic;

        -- Control Links
        start_actuation   : in    std_logic;
        target_pos        : in    unsigned(5 downto 0);
        current_pos       : out   unsigned(5 downto 0);
        actuation_busy    : out   std_logic;

        -- Hardware Interfaces
        flash_req_addr    : out   std_logic_vector(16 downto 0);
        flash_rx_data     : in    std_logic_vector(7 downto 0);
        flash_execute     : out   std_logic;
        flash_system_bsy  : in    std_logic;

        -- Stepping Interface
        homing_switch_pin : in    std_logic; 
        step_fwd_pin      : out   std_logic;
        step_rev_pin      : out   std_logic
    );
end actuation_controller;

architecture Behavioral of actuation_controller is
    type act_state_t is (ST_IDLE, ST_READ_POSITION, ST_WAIT_FLASH, ST_CALCULATE_PATH, 
                         ST_EXECUTE_STEP, ST_WAIT_MECHANICAL, ST_RECURSIVE_CHECK);
    signal current_state : act_state_t := ST_IDLE;

    signal internal_current : unsigned(5 downto 0) := (others => '0');
    signal step_countdown   : unsigned(5 downto 0) := (others => '0');
    signal inverted_switch  : std_logic := '0';
begin
    current_pos     <= internal_current;
    inverted_switch <= not homing_switch_pin; -- Flip active-low pin configuration
    process(clk, rst_n)
        variable path_delta : integer range -63 to 63 := 0;
    begin
        if rst_n = '0' then
            current_state    <= ST_IDLE;
            actuation_busy   <= '0';
            step_fwd_pin     <= '0';
            step_rev_pin     <= '0';
            flash_execute    <= '0';
            flash_req_addr   <= (others => '0');
            internal_current <= (others => '0');
            step_countdown   <= (others => '0');
        elsif rising_edge(clk) then
            case current_state is
                when ST_IDLE =>
                    step_fwd_pin  <= '0';
                    step_rev_pin  <= '0';
                    flash_execute <= '0';
                    if start_actuation = '1' then
                        actuation_busy <= '1';
                        current_state  <= ST_READ_POSITION;
                    else
                        actuation_busy <= '0';
                    end if;
                when ST_READ_POSITION =>
                    -- Access position map row sector (Forced all 1s)
                    flash_req_addr <= "11111111111" & std_logic_vector(target_pos);
                    flash_execute  <= '1'; 
                    current_state  <= ST_WAIT_FLASH;
                when ST_WAIT_FLASH =>
                    flash_execute <= '0';
                    if flash_system_bsy = '0' then
                        internal_current <= unsigned(flash_rx_data(5 downto 0));
                        current_state    <= ST_CALCULATE_PATH;
                    end if;
                when ST_CALCULATE_PATH =>
                    if internal_current = target_pos then
                        current_state <= ST_IDLE;
                    else
                        path_delta := to_integer(target_pos) - to_integer(internal_current);

                        ---------------------------------------------------
                        -- REMAPPED ROTATION SHORTEST PATH EVALUATION
                        ---------------------------------------------------
                        if (path_delta > 0 and path_delta <= 32) or (path_delta < -32) then
                            step_fwd_pin   <= '1';
                            step_rev_pin   <= '0';
                            step_countdown <= to_unsigned(abs(path_delta), 6);
                        else
                            step_fwd_pin   <= '0';
                            step_rev_pin   <= '1';
                            step_countdown <= to_unsigned(abs(path_delta), 6);
                        end if;
                        current_state <= ST_EXECUTE_STEP;
                    end if;
                when ST_EXECUTE_STEP =>
                    if step_countdown > 1 then
                        step_countdown <= step_countdown - 1;
                        current_state  <= ST_WAIT_MECHANICAL;
                    else
                        step_fwd_pin  <= '0';
                        step_rev_pin  <= '0';
                        current_state <= ST_RECURSIVE_CHECK;
                    end if;
                when ST_WAIT_MECHANICAL =>
                    current_state <= ST_EXECUTE_STEP;
                when ST_RECURSIVE_CHECK =>
                    if inverted_switch = '1' then
                        current_state <= ST_READ_POSITION; -- Recursive verification loopback path
                    end if;
                when others => current_state <= ST_IDLE;
            end case;
        end if;
    end process;
end Behavioral;