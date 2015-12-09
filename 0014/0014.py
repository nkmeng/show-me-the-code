# -*- coding: utf-8 -*-
"""
第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}
当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
"""
import xlwt

students_info = {
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}

def save_students_info(filename, info):
    file = xlwt.Workbook()
    table = file.add_sheet('students_info')
    line = 0
    for k, v in info.items():
        column = 0
        table.write(line, column, k)
        for i in v:
            column = column + 1
            table.write(line, column, i)
        line = line + 1
    file.save(filename)

if __name__ == '__main__':
    save_students_info('info.xls', students_info)