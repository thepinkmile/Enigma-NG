library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity data_processor is
    Port (
        clk              : in    std_logic;
        rst_n            : in    std_logic;
        token_flag       : inout std_logic;
        shared_data      : inout std_logic_vector(7 downto 0);

        -- Direct Interconnect Channels Heading Into Core Multiplexer
        flash_req_addr   : out   std_logic_vector(16 downto 0);
        flash_rx_data    : in    std_logic_vector(7 downto 0);
        flash_execute    : out   std_logic;
        flash_system_bsy : in    std_logic
    );
end data_processor;

architecture Behavioral of data_processor is
    type data_state_t is (ST_WAIT_TOKEN, ST_CALC_ADDR, ST_FETCH_FLASH, ST_RELEASE_TOKEN);
    signal current_state : data_state_t := ST_WAIT_TOKEN;
	 
    signal ring_offset_reg : unsigned(5 downto 0) := (others => '0');
    signal map_select_msb  : unsigned(10 downto 0) := (others => '0');
begin
    -------------------------------------------------------------------
    -- HIGH SPEED CHARACTER MATRIX SEQUENCER PROCESS
    -------------------------------------------------------------------
    process(clk, rst_n)
        variable full_addr_calc : unsigned(16 downto 0) := (others => '0');
        variable raw_char_input : unsigned(5 downto 0) := (others => '0');
    begin
        if rst_n = '0' then
            current_state   <= ST_WAIT_TOKEN;
            flash_execute   <= '0';
            flash_req_addr  <= (others => '0');
            ring_offset_reg <= (others => '0');
            map_select_msb  <= (others => '0');
        elsif rising_edge(clk) then
            flash_execute <= '0'; -- Clear lookup request pulse
            case current_state is
                when ST_WAIT_TOKEN =>
                    if token_flag = '0' then
                        current_state <= ST_CALC_ADDR;
                    end if;
                when ST_CALC_ADDR =>
                    -- Settle active-high bits from shared buffer matrix data slice
                    raw_char_input := unsigned(shared_data(5 downto 0));

                    -- Concatenate configuration MSBs with calculated lower offset values
                    full_addr_calc := map_select_msb & (raw_char_input + ring_offset_reg);
                    flash_req_addr <= std_logic_vector(full_addr_calc);
                    flash_execute  <= '1'; -- Launch immediate read stroke via default link
                    current_state  <= ST_FETCH_FLASH;
                when ST_FETCH_FLASH =>
                    if flash_system_bsy = '0' then
                        -- Secure true conversion code instantly out of the parallel lines
                        shared_data   <= flash_rx_data; 
                        current_state <= ST_RELEASE_TOKEN;
                    end if;
                when ST_RELEASE_TOKEN =>
                    token_flag    <= '1'; -- Relay baton token back over to I2C interface
                    current_state <= ST_WAIT_TOKEN;
                when others => current_state <= ST_WAIT_TOKEN;
            end case;
        end if;
    end process;
end Behavioral;