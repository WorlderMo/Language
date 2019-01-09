# -*- coding: utf-8 -*-
# @Date    : 2018-07-05 11:28:55
# @Author  : mohailang (1198534595@qq.com)

import pandas as pd
import os
import glob
import re
import xlrd
import xlwt

# a = glob.iglob("/Users/worlder/Desktop/留宿申请/*.xls")
# for i in a:
#     print(i)
# b = os.listdir("/Users/worlder/Desktop/留宿申请")
# print(b)


def search_excel(path):

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            search_excel(item_path)
        elif os.path.isfile(item_path):
            if re.search('.xls', item_path):
                xlsList.append(item_path)


def read_excel(xlsList):
    for xls in xlsList:
        data = xlrd.open_workbook(xls)
        table = data.sheets()[0]
        rows = table.nrows
        for i in range(5, rows):
            xlsContent.append(table.row_values(i))


def write_excel(xlsContent):
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet('留校汇总')

    xlsListLen = len(xlsContent)
    xlsContentLen = len(xlsContent[0])
    for i in range(0, xlsListLen):
        for j in range(0, xlsContentLen):
            worksheet.write(i, j, xlsContent[i][j])
    workbook.save("留校汇总2019.xls")


# 筛选，避免重复
def seclect(lists):
    afterContent = []
    for i in lists:
        if not i in afterContent:
            afterContent.append(i)
    return afterContent


if __name__ == '__main__':
    xlsList = []
    xlsContent = []
    path = "/Users/worlder/Desktop/留宿2019"
    search_excel(path)
    read_excel(xlsList)
    write_excel(seclect(xlsContent))
    for i in seclect(xlsContent):
        print(i)
