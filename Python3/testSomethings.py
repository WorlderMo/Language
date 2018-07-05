import pandas as pd
import xlrd
import xlwt

data = xlrd.open_workbook("/Users/worlder/Desktop/留宿申请/3631留宿申请汇总.xls")
table = data.sheets()[0]
rows = table.nrows
a = table.row_values(5)

print(rows)
print(a)
# workbook = xlwt.Workbook()
# worksheet = workbook.add_sheet('My Worksheet')
# for i in range(0, len(a)):
#     worksheet.write(1, i, a[i])
# workbook.save("a.xls")
