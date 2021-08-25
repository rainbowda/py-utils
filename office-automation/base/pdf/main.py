import pdfplumber
pdf =  pdfplumber.open("test.pdf")
# 访问第二页
print(pdf)
print(len(pdf.pages))
# 第一页pdfplumber.Page实例
first_page = pdf.pages[0]
# 查看页码
print('页码：',first_page.page_number)
# 查看页宽
print('页宽：',first_page.width)
# 查看页高
print('页高：',first_page.height)

