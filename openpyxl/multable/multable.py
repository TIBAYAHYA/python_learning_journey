import openpyxl,sys,pyperclip,os
#############################cmd liner##############################
if len(sys.argv) > 1:
    numeroto = " ".join(sys.argv[1:])
else:
    numeroto = pyperclip.paste()
numeroto = int(numeroto)
############################spread sheet############################
wb = openpyxl.Workbook()
sheet = wb.active
####################################################################
sheet.cell(row=1,column=1).value= "N="+str(numeroto) #this is the top left number disc
for ro_w in range(1,numeroto+1):   
    sheet.cell(row=1,column=ro_w+1).value = ro_w
    sheet.cell(row=ro_w+1,column=1).value = ro_w
    for col in range(1,numeroto+1):    
        sheet.cell(row=ro_w+1,column=col+1).value = ro_w * col
os.chdir(r"C:\Users\maroc\OneDrive\Desktop\coding journey\python\openpyxl")
wb.save("multable.xlsx")