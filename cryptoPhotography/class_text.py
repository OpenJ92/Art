import string
import PyPDF2
# tkia
from itertools import cycle

class TEXT():
    def __init__(self, pdfPATH):
        self.pdfPATH = pdfPATH
        self.text = self.extractText().lower()
        self.cycletext = cycle(self.text)

    def extractText(self):
        pdfFileObj = open(self.pdfPATH, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        str_ = ''

        for page in range(0,pdfReader.numPages):
            str_ += pdfReader.getPage(page).extractText()
        return str_
