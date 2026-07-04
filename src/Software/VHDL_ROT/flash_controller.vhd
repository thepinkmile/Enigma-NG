library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity flash_controller is
    Port (
        clk              : in    std_logic;
        rst_n            : in    std_logic;
        req_address      : in    std_logic_vector(16 downto 0);
        out_data_byte    : out   std_logic_vector(7 downto 0);
        start_read_pulse : in    std_logic;
        controller_busy  : out   std_logic;

        -- Direct Hardware Device Leg Connections
        flash_addr_pins  : out   std_logic_vector(16 downto 0);
        flash_data_pins  : inout std_logic_vector(7 downto 0);
        flash_oe_n       : out   std_logic; 
        flash_we_n       : out   std_logic; 
        flash_ce_n       : out   std_logic
    );
end flash_controller;

architecture Behavioral of flash_controller is
    type flash_state_t is (ST_READY, ST_DRIVE_BUS, ST_HOLD_DELAY, ST_READ_LATCH);
    signal f_state : flash_state_t := ST_READY;
begin
    flash_data_pins <= (others => 'Z'); -- Establish reading high-impedance mode defaults

    process(clk, rst_n)
        variable delay_timer : integer range 0 to 7 := 0;
    begin
        if rst_n = '0' then
            f_state         <= ST_READY;
            flash_ce_n      <= '1'; -- Park active-low control gates high during reset
            flash_we_n      <= '1';
            flash_oe_n      <= '1';
            flash_addr_pins <= (others => '0');
            controller_busy <= '0';
        elsif rising_edge(clk) then
            case f_state is
                when ST_READY =>
                    controller_busy <= '0';
                    flash_ce_n      <= '1';
                    flash_oe_n      <= '1';
                    if start_read_pulse = '1' then
                        flash_addr_pins <= req_address;
                        controller_busy <= '1';
                        f_state         <= ST_DRIVE_BUS;
                    end if;
                when ST_DRIVE_BUS =>
                    flash_ce_n  <= '0'; -- Wake chip up
                    flash_oe_n  <= '0'; -- Trigger output read trace parameters
                    delay_timer := 3;
                    f_state     <= ST_HOLD_DELAY;
                when ST_HOLD_DELAY =>
                    if delay_timer > 0 then delay_timer := delay_timer - 1;
                    else f_state <= ST_READ_LATCH; end if;
                when ST_READ_LATCH =>
                    out_data_byte   <= flash_data_pins;
                    flash_ce_n      <= '1';
                    flash_oe_n      <= '1';
                    f_state         <= ST_READY;
                when others => f_state <= ST_READY;
            end case;
        end if;
    end process;
end Behavioral;