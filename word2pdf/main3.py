from win32com.client import gencache
from win32com.client import constants, gencache

import sys
from tkinter import *
from tkinter import ttk

def createPdf(wordPath, pdfPath):
    word = gencache.EnsureDispatch('Word.Application')
    doc = word.Documents.Open(wordPath, ReadOnly=1)
    doc.ExportAsFixedFormat(pdfPath,
                            constants.wdExportFormatPDF,
                            Item=constants.wdExportDocumentWithMarkup,
                            CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
    word.Quit(constants.wdDoNotSaveChanges)


# see https://www.runoob.com/python/python-gui-tkinter.html
def createWindow():
    # 1.窗口
    root= Tk()
    root.title('word转pdf工具')
    #root.geometry('300x400') # 这里的乘号不是 * ，而是小写英文字母 x

    # 2.布局 三杭三列
    mainframe = ttk.Frame(root, padding="10 15 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)


    # 3.输入输出按钮
    ttk.Label(mainframe, text="word文件位置").grid(column=1, row=1, sticky=W,padx=10,pady=10)
    inputFilePath = StringVar()
    inputFilePathEntry = ttk.Entry(mainframe, width=20, textvariable=inputFilePath)
    inputFilePathEntry.grid(column=2, row=1, sticky=(W, E),padx=10)
    ttk.Button(mainframe, text="选择", command=createPdf).grid(column=3, row=1, sticky=E)


    ttk.Label(mainframe, text="pdf输出文件位置").grid(column=1, row=2, sticky=E,pady=10)
    outputFilePath = StringVar()
    outputFilePathEntry = ttk.Entry(mainframe, width=20, textvariable=outputFilePath)
    outputFilePathEntry.grid(column=2, row=2, sticky=(W, E),padx=10)
    ttk.Button(mainframe, text="选择", command=createPdf).grid(column=3, row=2, sticky=E)


    # 4.开始按钮
    ttk.Button(mainframe, text="转换", width=30, command=lambda: createPdf(inputFilePathEntry.get(),outputFilePathEntry.get())).grid(column=2, row=3,sticky=E,padx=40,pady=20)

    root.mainloop()# 进入消息循环


# py .\main2.py test.docx test.pdf
if __name__ == "__main__":
   #createPdf(sys.argv[1],sys.argv[2])
   createWindow()


