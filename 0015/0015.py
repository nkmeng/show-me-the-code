# -*- coding: utf-8 -*-
"""
第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}
"""
import xlwt
import json
from collections import OrderedDict

def read_txt(file):
    with open(file) as f:
        txt = f.read()
    return json.loads(txt, object_pairs_hook=OrderedDict)

def save_city_info(xls, info):
    file = xlwt.Workbook()
    table = file.add_sheet('city_info')
    line = 0
    for k, v in info.items():
        column = 0
        table.write(line, column, k)
        column = column + 1
        table.write(line, column, v)
        line = line + 1
    file.save(xls)

def txt_to_xls(txt, xls):
    info = read_txt(txt)
    save_city_info(xls, info)

if __name__ == '__main__':
    txt_to_xls('city.txt', 'city.xls')