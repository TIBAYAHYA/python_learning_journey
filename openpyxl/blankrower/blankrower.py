import openpyxl
linera = input("enter the secret sauce:\n")
linera = linera.split(" ")
file_name = linera[2]
first_index = int(linera[0])
second_index = int(linera[1])
wb = openpyxl.open(file_name)
sheet = wb.active
for x in range(first_index,first_index+second_index):
    for y in range(sheet.min_column,sheet.max_column+1):
        sheet.cell(row=x,column=y).value = None
new_filename = file_name.replace(".xlsx","blanked.xlsx")
wb.save(new_filename)