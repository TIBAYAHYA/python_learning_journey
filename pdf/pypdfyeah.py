import PyPDF2 as pdf
pdf_file = open("meetingminutes.pdf","rb")
pdf_file2 = open("meetingminutes2.pdf","rb")
pdf_reader = pdf.PdfReader(pdf_file)
pdf_reader2 = pdf.PdfReader(pdf_file2)
pdf_writer = pdf.PdfWriter()
pages = pdf_reader.pages
pages2 = pdf_reader2.pages
for page in pages:
    pdf_writer.add_page(page)
for page2 in pages2:
    pdf_writer.add_page(page2)
pdf_writer.pages[0].rotate(90)
out_put_file = open("meetingminutes_adjusted.pdf","wb")
pdf_writer.write(out_put_file)


pdf_file.close()
pdf_file2.close()
out_put_file.close()
