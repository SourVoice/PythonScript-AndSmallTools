import os

tel_content = open('tel.txt', "r", encoding='gbk')
name_content = open('name.txt', "r", encoding='utf-8')
tel = []
name = []
tel_name = []
i = 2
for line in tel_content:
    if i % 2 == 0:
        i = i + 1
    else:
        tel.append(line.split('\n')[0])
        i = i + 1
print(tel)

i = 2
for line in name_content:
    if i % 2 == 0:
        i = i + 1
    else:
        name.append(line.split('\n')[0])
        i = i + 1
for each_tel, each_name in zip(tel, name):
    tel_name.append(each_tel + ' ' + each_name)
print(tel_name)
tel.append('13275103356')

# import xlwt
#
# f = xlwt.Workbook()  # 工作簿
#
# sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
#
# for i in range(len(tel)):
#     sheet1.write(0, i, i)  # 表格的第一行开第一列，列。。。。
#
# # sheet1.write(0,0,start_date,set_style('Times New Roman',220,True))
#
# f.save('text.xls')  # 保存文件
import pandas as pd

dataframe = pd.DataFrame(list(tel_name))

print(dataframe)

dataframe.to_excel('tel_name.xlsx')
