'''
Author: CYLlinmaian
Date: 2022-07-10 12:07:53
LastEditTime: 2022-07-10 12:18:10
LastEditors: CYLlinmaian
Description: 
FilePath: \Big Job\Automatic trajectory drawing.py
Copyright © 1999 - 2022 Mr.chen.All Rights Reserved.
'''
import turtle as t

t.title("陈勇林——轨迹绘制")
t.setup(800, 600, 0, 0)  # 画布大小
t.pencolor("red")  # 画笔颜色
t.pensize(5)  # 画笔宽度
# 数据读取
datals = []
f = open("轨迹绘制.txt", encoding='UTF-8')  # 注意用斜杠来表示地址
for line in f:  # 遍历文件
    line = line.replace("\n", "")  # 将每行最后的换行符用空格来代替
    datals.append(list(map(eval, line.split(","))))
f.close()  # 见下面详解
# 自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3], datals[i][4], datals[i][5])  # 读取画笔颜色
    t.fd(datals[i][0])  # 读取行进距离
    if datals[i][1]:  # 判断转向，为 1 则右转
        t.right(datals[i][2])  # 右转角度
    else:  # 为 0 则左转
        t.left(datals[i][2])
