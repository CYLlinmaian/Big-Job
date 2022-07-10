'''
Author: CYLlinmaian
Date: 2022-07-10 12:07:51
LastEditTime: 2022-07-10 12:15:53
LastEditors: CYLlinmaian
Description: 
FilePath: \Big Job\magic square.py
Copyright © 1999 - 2022 Mr.chen.All Rights Reserved.
'''
import random
import turtle


# 写一个随即色的函数，将颜色存在列表中，进行颜色的随机遍历
def random_color():
    color_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                  'A', 'B', 'C', 'D', 'E', 'F']
    color = ''
    for i in range(6):
        color_number = color_list[random.randint(0, 15)]
        color += color_number
    color = '#' + color
    return color


def draw_square():  # 小方块绘制函数
    for i in range(4):
        turtle.forward(47)
        turtle.right(90)


def main():  # 主函数，引用前面的自定义函数模块，绘制6x6小方块
    a = 55
    for i in range(6):
        x = 0  # x,y确定绘制的起始位置
        y = (i + 1) * a
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(random_color())  # 正方形颜色随机
        turtle.begin_fill()
        draw_square()
        turtle.end_fill()
    for i in range(6):
        x = -a
        y = (i + 1) * a
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(random_color())  # 正方形颜色随机
        turtle.begin_fill()
        draw_square()
        turtle.end_fill()
    for i in range(6):
        x = -(a * 2)
        y = (i + 1) * a
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(random_color())  # 正方形颜色随机
        turtle.begin_fill()
        draw_square()
        turtle.end_fill()
    for i in range(6):
        x = -(a * 3)
        y = (i + 1) * a
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(random_color())  # 正方形颜色随机
        turtle.begin_fill()
        draw_square()
        turtle.end_fill()
    for i in range(6):
        x = -(a * 4)
        y = (i + 1) * a
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(random_color())  # 正方形颜色随机
        turtle.begin_fill()
        draw_square()
        turtle.end_fill()
    for i in range(6):
        x = -(a * 5)
        y = (i + 1) * a
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(random_color())  # 正方形颜色随机
        turtle.begin_fill()
        draw_square()
        turtle.end_fill()
    turtle.exitonclick()


if __name__ == '__main__':
    main()
