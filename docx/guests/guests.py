import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH

guests_txt = open('guests.txt', 'r')
guests = guests_txt.read()
guests = guests.split('\n')
invites_document = docx.Document()
for guest in guests:
    paragraph = invites_document.add_paragraph("It would be a pleasure to have the company of: ")
    run = paragraph.runs[0]
    run.italic = True
    run.font.size = docx.shared.Pt(20)
    run.font.name = 'Arial'
    paragraph = invites_document.add_paragraph(guest)
    run = paragraph.runs[0]
    run.bold = True
    run.font.size = docx.shared.Pt(30)
    paragraph = invites_document.add_paragraph()
    run1 = paragraph.add_run("at ")
    run1.bold = True
    run1.underline = True
    run1.font.size = docx.shared.Pt(20)
    run2 = paragraph.add_run(" 11010 ")
    run2.italic = True
    run2.font.size = docx.shared.Pt(20)
    run3 = paragraph.add_run("memory run at the evening of")
    run3.bold = True
    run3.font.size = docx.shared.Pt(20)
    paragraph = invites_document.add_paragraph()
    run1 = paragraph.add_run("April 1st")
    run1.font.size = docx.shared.Pt(20)
    paragraph = invites_document.add_paragraph()
    run1 = paragraph.add_run("at ")
    run1.font.size = docx.shared.Pt(20)

    run1.underline = True
    run1.bold = True
    run1.font.size = docx.shared.Pt(20)
    run2 = paragraph.add_run("7 o\"clock")
    run2.font.size = docx.shared.Pt(20)
    paragraph.add_run().add_break(docx.text.run.WD_BREAK.PAGE)

for paragraph in invites_document.paragraphs:
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

invites_document.save("documanta.docx")
