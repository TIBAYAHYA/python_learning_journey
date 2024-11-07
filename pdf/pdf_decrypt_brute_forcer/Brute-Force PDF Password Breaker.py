import os,sys
import PyPDF2 as pdf


os.chdir(r"C:\Users\maroc\OneDrive\Desktop\coding journey\automate_online-materials") #chdir to english words txt
english_words = open("dictionary.txt","r")
english_words = english_words.read()
english_words = english_words.split("\n")
os.chdir(r"C:\Users\maroc\OneDrive\Desktop\coding journey\python\pdf\pdf_decrypt_brute_forcer")
pdf_reader = pdf.PdfReader("this_is_an_empty_pdf_file.pdf") 




for english_word in english_words:
    pdf_reader.decrypt(english_word)
    if pdf_reader.decrypt(english_word):
        print("The password is: ",english_word)
        sys.exit()
#AARHUS is tha password