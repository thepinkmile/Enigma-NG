library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity cpld_rotor_core is
    Port (
        -- Physical CPLD External Clock and Reset Pins
        clk_pin : in std_logic;
        rst_n_pin : in std_logic;
        
        -- Physical I2C Bus Pins
        i2c_addr_in : in std_logic_vector(6 downto 0);
        i2c_addr_out : out std_logic_vector(6 downto 0);
        sda_pin : inout std_logic;
        scl_pin : in std_logic;
        
        -- Physical External Parallel Flash Memory Pins
        flash_addr_pin : out std_logic_vector(16 downto 0);
        flash_data_pin : inout std_logic_vector(7 downto 0);
        flash_oe_n_pin : out std_logic;
        flash_we_n_pin : out std_logic;
        flash_ce_n_pin : out std_logic;
        
        -- Physical Shroud Tracking Hardware Interface
        homing_sw_pin : in std_logic;
        
        -- Independent Active-High Solenoid Driver Output Pins
        step_fwd_pin : out std_logic;
        step_rev_pin : out std_logic
    );
end cpld_rotor_core;

architecture Structural of cpld_rotor_core is
    -------------------------------------------------------------------
    -- INTERNAL BUS WIRE DEFINITIONS (Virtual Copper Tracks)
    -------------------------------------------------------------------
    signal wire_token_flag : std_logic := '1'; -- Shared token boundary
    signal wire_shared_data : std_logic_vector(7 downto 0) := (others => '0');
    
    -- Priority Flash Access Arbiter
    signal i2c_flash_request : std_logic := '0';
    signal i2c_flash_addr : std_logic_vector(16 downto 0) := (others => '0');
    signal i2c_flash_req : std_logic := '0';
    signal i2c_flash_busy : std_logic;
    
	 -- Data Processor Flash Access Arbiter
    signal proc_flash_addr : std_logic_vector(16 downto 0) := (others => '0');
    signal proc_flash_req : std_logic := '0';
    signal proc_flash_busy : std_logic;
    
	 -- Master Flash Access
    signal wire_flash_addr : std_logic_vector(16 downto 0);
    signal wire_flash_rdata : std_logic_vector(7 downto 0);
    signal wire_flash_req : std_logic;
    signal wire_flash_busy : std_logic;
begin
	-------------------------------------------------------------------
    -- PRIORITY FLASH ACCESS BUS MULTIPLEXER (ARBITER)
    -------------------------------------------------------------------
	wire_flash_addr <= i2c_flash_addr when (i2c_flash_request = '1') else proc_flash_addr;
	wire_flash_req <= i2c_flash_req when (i2c_flash_request = '1') else proc_flash_req;
	proc_flash_busy <= '1' when (i2c_flash_request = '1') else wire_flash_busy;
	i2c_flash_busy <= wire_flash_busy when (i2c_flash_request = '1') else '1';
	
	i2c_addr_out <= i2c_addr_in + 1;

    U_I2C : entity work.i2c_controller
    port map (
        clk => clk_pin,
        rst_n => rst_n_pin,
		  
        i2c_addr => i2c_addr_in,
        sda => sda_pin,
        scl => scl_pin,
		  
        token_flag => wire_token_flag,
        shared_data => wire_shared_data,
		  
        -- Actuator Pins Routed through I2C as Primary Motion Controller
        homing_switch => homing_sw_pin,
        step_fwd => step_fwd_pin,
        step_rev => step_rev_pin,
		  
        -- Local Flash Controller Priority Request Bus
        flash_request_out => i2c_flash_request,
        flash_addr_out => i2c_flash_addr,
        flash_req_pulse => i2c_flash_req,
        flash_system_bsy => i2c_flash_busy
    );

    U_DATA_PROCESSOR : entity work.data_processor
    port map (
        clk => clk_pin,
        rst_n => rst_n_pin,
		  
        token_flag => wire_token_flag,
        shared_data => wire_shared_data,
		  
        -- Interconnect Channels Leading Into Top-Level Multiplexer
        flash_req_addr => proc_flash_addr,
        flash_rx_data => wire_flash_rdata,
        flash_execute => proc_flash_req,
        flash_system_bsy => proc_flash_busy
    );

    U_FLASH : entity work.flash_controller
    port map (
        clk => clk_pin,
        rst_n => rst_n_pin,
		  
        req_address => wire_flash_addr,
        out_data_byte => wire_flash_rdata,
        start_read_pulse => wire_flash_req,
        controller_busy => wire_flash_busy,
		  
        flash_addr_pins => flash_addr_pin,
        flash_data_pins => flash_data_pin,
        flash_oe_n => flash_oe_n_pin,
        flash_we_n => flash_we_n_pin,
        flash_ce_n => flash_ce_n_pin
    );

end Structural;