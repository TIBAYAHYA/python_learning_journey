import docx, os
os.chdir(r"C:\Users\maroc\OneDrive\Desktop\coding journey\automate_online-materials")
doc = docx.Document()   #starting a nameless docx file in the program
doc.add_paragraph("good morning my neighbors")# just adding a paragraph
doc.add_picture("zophie.png",width=docx.shared.Inches(2),height=docx.shared.Cm(5)) #this function add an image
doc.paragraphs[1].runs[0].add_break(docx.enum.text.WD_BREAK.PAGE) #this function skips the current page blanks and goes to the next
doc.add_paragraph("hello my friend")

os.chdir(r"C:\Users\maroc\OneDrive\Desktop\coding journey\python\docx")
doc.save("something_quite_unusual.docx")


