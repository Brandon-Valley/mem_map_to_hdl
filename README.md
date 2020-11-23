# mem_map_to_hdl

## Required Software

* Python 3.7+
* Visual Studio Code

## Description

---

Tool for easily converting a .csv memory map to hdl declarations

## Usage

---

1. Create **MEM_MAP.csv**
   1. Copy-Paste the **Register Offset** and **Register Name** columns into `<ABS PATH TO THIS REPO>/MEM_MAP.csv`
   2. Make sure there is no strange formatting, like extended cells
2. Configure [main.py](main.py)  
   1. Set `REG_OFFSET_HEADER` = the name of your register offset column header in **MEM_MAP.csv**
   2. Set `REG_NAME_HEADER` = the name of your register name column header in **MEM_MAP.csv**
   3. Set `REG_NAME_HEADER` = the name of your register name column header in **MEM_MAP.csv**
   4. Edit `REG_NAME_REPLACE_D` to include any additional strings that should be replaced in the register names
        * The string on the left will be replaced with the string on the right
   5. Edit the `hdl_line =` line in `get_hdl_line_l()` to match your desired formatting.
3. Run [main.py](main.py) - The output will open in **Visual Studio Code**

## Example

---

Input: `MEM_MAP.csv`

Register Offset | Name
----------------|------
0x000           | Module ID
0x004           | Version Number
0x008           | Clock Frequency
0x00C           | Status Register
0x018           | Interrupt Enable Register
0x080           | Safety Check Register

Output: `OUTPUT.sv`

```systemverilog
`define ADDR__TIMER__MODULE_ID            `ADDR__TIMER + 32'h0
`define ADDR__TIMER__VER_NUM              `ADDR__TIMER + 32'h4
`define ADDR__TIMER__CLOCK_FREQ           `ADDR__TIMER + 32'h8
`define ADDR__TIMER__STATUS_REG           `ADDR__TIMER + 32'hC
`define ADDR__TIMER__INTERRUPT_ENABLE_REG `ADDR__TIMER + 32'h18
`define ADDR__TIMER__SAFETY_CHECK         `ADDR__TIMER + 32'h80
```
