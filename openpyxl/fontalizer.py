import openpyxl
import openpyxl.chart
import openpyxl.chart.series
wb = openpyxl.Workbook()
sheet = wb.active
for x in range(1,11):
    sheet["A%s"%x] = x                  
ref_obj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1,max_col=1, max_row=10)
series_obj = openpyxl.chart.Series(ref_obj,title="yeah buddy")
chart_obj = openpyxl.chart.BarChart()
chart_obj.title = "My damned chart"
chart_obj.append(series_obj)
sheet.add_chart(chart_obj,"C5")
wb.save("sampleChart.xlsx")
