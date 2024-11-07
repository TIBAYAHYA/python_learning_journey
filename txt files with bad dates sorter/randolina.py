import os
from pathlib import Path
import re
import shutil
#############################################################
#this program opens 30 .txt file that have murican dates as a name
cwd = os.getcwd()
file_path = Path(cwd)
print(file_path)
for x in range(31):
    open(Path(file_path)/f"07-{x+1:02}-2004.txt","w")

##############################################################
#this program replaces murican format dates with european format
#aka MM/DD/YYYY into DD/MM/YYYY
murica_date = re.compile(r"""^(.*?) # pre date
                         ((1|0)?\d)- # month
                         ((3|2|1|0)?\d)- # day
                         (\d{4}) # year
                         (.*?)$ # after date
                        """, re.VERBOSE)
for file in os.listdir(file_path):
    if murica_date.search(file):
        mo = murica_date.search(file)
        pre_date = mo.group(1)
        month = mo.group(2)
        day = mo.group(4)
        year = mo.group(6)
        post_date = mo.group(7)
        new_name = f"{pre_date}{day}-{month}-{year}{post_date}"
        new_file_path = file_path /new_name
        shutil.move(str(file_path/file),new_file_path)
        

                         






