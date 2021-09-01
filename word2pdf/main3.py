from win32com.client import gencache
from win32com.client import constants, gencache

import sys
from tkinter import *

def createPdf(wordPath, pdfPath):
    word = gencache.EnsureDispatch('Word.Application')
    doc = word.Documents.Open(wordPath, ReadOnly=1)
    doc.ExportAsFixedFormat(pdfPath,
                            constants.wdExportFormatPDF,
                            Item=constants.wdExportDocumentWithMarkup,
                            CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
    word.Quit(constants.wdDoNotSaveChanges)


def createWindow():
    # 1.窗口
    root= Tk()
    root.title('word转pdf工具')
    root.geometry('360x240') # 这里的乘号不是 * ，而是小写英文字母 x

    # 2.布局

    # 3.输入输出男

    # 4.开始按钮

    root.mainloop()

# py .\main2.py test.docx test.pdf
if __name__ == "__main__":
   #createPdf(sys.argv[1],sys.argv[2])
   createWindow()


