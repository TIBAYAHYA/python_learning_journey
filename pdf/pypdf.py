import PyPDF2 as pdf
pdfFile = open("meetingminutes.pdf","rb")
pdfFile2 = open("meetingminutes2.pdf","rb")

reader = pdf.PdfReader(pdfFile)
reader2 = pdf.PdfReader(pdfFile2)
newPdf = pdf.PdfWriter()
read = (reader,reader2)
for red in read:
    for page_number in range(len(red.pages)):
        page = red.pages[page_number]
        newPdf.add_page(page)
new_pdf_file = open("combinedPdf.pdf","wb")
newPdf.write(new_pdf_file)
new_pdf_file.close()
pdfFile.close()
pdfFile2.close()