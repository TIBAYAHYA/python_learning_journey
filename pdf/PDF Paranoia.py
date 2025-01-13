import os
import PyPDF2
os.chdir(r"C:\Users\maroc\OneDrive\Desktop\coding journey\python\pdf")
cwd = os.getcwd()
target_dir = (r"C:\Users\maroc\OneDrive\Desktop\coding journey\python\pdf\PDF paranoia")

for rel_path, dirnames, filenames in os.walk("os_walk_example"):
    for pdf_file in filenames:
        abs_path = os.path.join(cwd,rel_path,pdf_file)
        pdf_reader = PyPDF2.PdfReader(abs_path)
        pdf_writer = PyPDF2.PdfWriter()
        for page_num in range(1,len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])
        pdf_writer.encrypt("pass")
        new_file_name = pdf_file[0:-4]+"_encrypted.pdf"
        new_file_name = os.path.join(target_dir,new_file_name)
        
        with open(new_file_name,"wb") as finlanda:
            pdf_writer.write(finlanda)
        
        
        
