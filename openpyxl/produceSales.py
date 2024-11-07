import openpyxl
wb = openpyxl.load_workbook("produceSales.xlsx")
sheet = wb.active
PRICE_UPDATES = {'Garlic': 3.07,
                 'Celery': 1.19,
                 'Lemon': 1.27}

for x in range(2,sheet.max_row+1):
    current_cell_value = sheet.cell(row=x,column=1).value
    if current_cell_value in PRICE_UPDATES:
        sheet.cell(row=x,column=2).value = PRICE_UPDATES[current_cell_value]
wb.save("produceSales_versionata.xlsx")