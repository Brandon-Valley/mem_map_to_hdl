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
   3. Edit the `hdl_line =` line in `get_hdl_line_l()` to match your desired formatting.
3. Run [main.py](main.py) - The output will open in **Visual Studio Code**
