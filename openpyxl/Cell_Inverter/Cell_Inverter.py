import openpyxl
wb =openpyxl.open("censuspopdata.xlsx")
sheet = wb.active
cells_data=[]
for co_l in range(sheet.min_column,sheet.max_column+1):
    for ro_w in range(sheet.min_row,sheet.max_row+1):
        cells_data.append((sheet.cell(row=ro_w,column=co_l).value,ro_w,co_l))
        sheet.cell(row=ro_w,column=co_l).value = None
print(cells_data)
for cell_data in cells_data:
    sheet.cell(row=cell_data[2],column=cell_data[1]).value = cell_data[0]
wb.save("censuspopdata_inverted.xlsx")