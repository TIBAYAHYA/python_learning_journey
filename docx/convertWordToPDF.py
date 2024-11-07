# This script runs on Windows only, and you must have Word installed.
from docx2pdf import convert
import docx
wordFilename = 'something_quite_unusual.docx'
pdfFilename = 'something_quite_unusual.pdf'
convert(wordFilename, pdfFilename)
