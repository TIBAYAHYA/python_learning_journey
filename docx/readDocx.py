#this code prints the content of a docx file



import docx,os
def getText(filename):
    os.chdir(r"C:\Users\maroc\OneDrive\Desktop\coding journey\automate_online-materials")
    doc = docx.Document(filename)
    doca = []
    for paragraph in doc.paragraphs:
        doca.append(paragraph.text)
    return "\n".join(doca)
print(getText("demo.docx"))
