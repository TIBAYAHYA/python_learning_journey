import openpyxl
wb = openpyxl.open("xlsx_to_txt.xlsx")
sheet = wb.active
for co_l in range(sheet.min_column,sheet.max_column+1):
    with open(str(co_l)+".txt","w") as txt_file:
        for ro_w in range(sheet.min_row,sheet.max_row+1):
            txt_file.write(sheet.cell(row=ro_w,column=co_l).value+"\n")
            