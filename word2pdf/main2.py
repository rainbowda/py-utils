from win32com.client import gencache
from win32com.client import constants, gencache

import sys

def createPdf(wordPath, pdfPath):
    word = gencache.EnsureDispatch('Word.Application')
    doc = word.Documents.Open(wordPath, ReadOnly=1)
    doc.ExportAsFixedFormat(pdfPath,
                            constants.wdExportFormatPDF,
                            Item=constants.wdExportDocumentWithMarkup,
                            CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
    word.Quit(constants.wdDoNotSaveChanges)



# see https://www.runoob.com/python/python-command-line-arguments.html
# py .\main2.py test.docx test.pdf
if __name__ == "__main__":
   createPdf(sys.argv[1],sys.argv[2])


