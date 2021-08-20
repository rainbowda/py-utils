import xlwings as xw
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

wb = xw.Book("example.xlsx")
# 实例化工作表对象
sht = wb.sheets["sheet1"]
# 在单元格中写入数据
sht.range('A1').value = "test"

# 给单元格上背景色，传入RGB值
sht.range('A1').color = (34,139,34)

#输入公式，相应单元格会出现计算结果
sht.range('A1').formula='=SUM(B6:B7)'

#获取单元格公式
sht.range('A1').formula_array
#写入numpy array数据类型
np_data = np.array((1,2,3))
sht.range('F1').value = np_data

#支持将pandas DataFrame数据类型写入excel
df = pd.DataFrame([[1,2], [3,4]], columns=['a', 'b'])
sht.range('A5').value = df

# 将数据读取，输出类型为DataFrame
sht.range('A5').options(pd.DataFrame,expand='table').value

# 将matplotlib图表写入到excel表格里
#%matplotlib inline
#fig = plt.figure()
#plt.plot([1, 2, 3, 4, 5])
#sht.pictures.add(fig, name='MyPlot', update=True)