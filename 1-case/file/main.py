with open('text.txt','r+') as f: # r：表示文件只能读取 w：表示文件只能写入 a：表示打开文件，在原有内容的基础上追加内容，在末尾写入 w+:表示可以对文件进行读写双重操作
    data = f.read()
    print(data)
    f.write("\n666") # f为文件对象
    f.close()


print("-----------------------------------------")
# 操作csv文件
import csv
with open('test.csv','r+',encoding="utf-8") as myFile:
    # 读取
    lines=csv.reader(myFile)
    for line in lines:
        print(line)

    #写入
    myWriter=csv.writer(myFile)
    # writerrow一行一行写入
    myWriter.writerow([7,8,9])
    myWriter.writerow([8,'h','f'])
    # writerow多行写入
    myList=[[1,2,3],[4,5,6]]
    myWriter.writerows(myList)


# 使用numpy库（loadtxt、load、fromfile）

import numpy as np
# loadtxt()中的dtype参数默认设置为float
# 这里设置为str字符串便于显示
np.loadtxt('test.csv',dtype=str)
# out：array(['1,2,3', '4,5,6', '7,8,9'], dtype='<U5')

# 先生成npy文件
np.save('test.npy', np.array([[1, 2, 3], [4, 5, 6]]))
# 使用load加载npy文件
np.load('test.npy')
'''
out:array([[1, 2, 3],
       [4, 5, 6]])
'''
x = np.arange(9).reshape(3,3)
x.tofile('test.bin')
np.fromfile('test.bin',dtype=np.int)
# out:array([0, 1, 2, 3, 4, 5, 6, 7, 8])