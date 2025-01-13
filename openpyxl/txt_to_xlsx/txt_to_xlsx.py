import openpyxl

txt_files = []
for x in range(1,5):
    txt_files.append((str(x)+".txt"))
wb = openpyxl.Workbook()
sheet = wb.active
for txt_file_index,txt_file in enumerate(txt_files):
   with open(txt_file) as file_content:
        file_content = file_content.read()
        file_line = file_content.split("\n")
        for line_index,line_value in enumerate(file_line):
            print(line_value)
            sheet.cell(row=line_index+1,column=txt_file_index+1).value = line_value
wb.save("txt_to_xlsx.xlsx")