#this program combines all pdf files in the directory 
#exept for the first page in pdf files after 1st pdf file

#########################################################################################################################################################################
# this part fo the code save files that end with .pdf extension into a variable named pdf_files_names
#and sorts them
import os,PyPDF2 as pdf
pdf_files_names_list = []
for file in os.listdir():
    if file.endswith(".pdf"):
        pdf_files_names_list.append(file)

pdf_files_names_list.sort()
####################################################################################################################################################################################
pdfs_writer = pdf.PdfWriter()


for pdf_file_name in pdf_files_names_list:
    file_opening = open(pdf_file_name,"rb")
    reader = pdf.PdfReader(file_opening)
    pages = reader.pages
    for indexa,page in enumerate(pages):
        if pdf_file_name != pdf_files_names_list[0]:#If It is NOT the first file
            if indexa != 0:                    #If It is not the first page             
                pdfs_writer.add_page(page)          # Write It down
        elif pdf_file_name == pdf_files_names_list[0]:
            pdfs_writer.add_page(page)            # If It is the first page write It all
    file_opening.close()
                
outputfile = open("pdf_combined.pdf","wb")
pdfs_writer.write(outputfile)
outputfile.close()  # Close the output file

