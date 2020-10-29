import os.path as path

from sms.logger import logger



MEM_MAP_CSV_PATH = path.join( path.abspath(path.dirname(__file__)), 'MEM_MAP.csv')

REG_OFFSET_HEADER = 'Register Offset'
REG_NAME_HEADER   = 'Name'



print('Memory map CSV path:  ', MEM_MAP_CSV_PATH) 

row_dl = logger.readCSV(MEM_MAP_CSV_PATH)
print(row_dl)

if row_dl == []:
    raise Exception("ERROR:  " + MEM_MAP_CSV_PATH + " is an empty spreadsheet, copy-paste the memory map you would like to use into this file")


converted_str_l = []

# get offset_name_dl
def get_offset_name_dl():
    offset_name_dl = []
    for row_d in row_dl:
        og_reg_offset_str = row_d[REG_OFFSET_HEADER]
        og_reg_name_str   = row_d[REG_NAME_HEADER]
        
        # format reg_offset_str
        reg_offset_str = og_reg_offset_str.replace('0x', '')
        print('reg_offset_str: ', reg_offset_str)
        
        # format reg_name_str
        reg_name_str = og_reg_name_str.replace(' ', '_').upper()
        print('reg_name_str: ', reg_name_str)
        
        offset_name_dl.append({'offset' : reg_offset_str,
                                   'name'   : reg_name_str})
    return offset_name_dl
        
        
def get_longest_name_len(offset_name_dl):
    longest_name_len = 0
    
    for offset_name_d in offset_name_dl:
        name_len = len(offset_name_d['name'])
        
        if name_len > longest_name_len:
            longest_name_len = name_len
    
    return longest_name_len
    

    
#     print('`define ')

    converted_str = '`define ADDR__CUR_UART__{} '
    
    
for converted_str in converted_str_l:
    print('converted_str: ', converted_str)

print('Getting offset_name_dl...')
offset_name_dl = get_offset_name_dl()

print('Getting longest_name_len...')
longest_name_len = get_longest_name_len(offset_name_dl)

print(longest_name_len)







print('done')