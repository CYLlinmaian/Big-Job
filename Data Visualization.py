'''
Author: CYLlinmaian
Date: 2022-07-10 12:07:51
LastEditTime: 2022-07-10 12:16:33
LastEditors: CYLlinmaian
Description: 
FilePath: \Big Job\Data Visualization.py
Copyright © 1999 - 2022 Mr.chen.All Rights Reserved.
'''
import math

import matplotlib.pyplot as plt
import numpy as np


def gd(x, m, s):  # 其中s为sigma ,m为 mu
    left = 1 / (math.sqrt(2 * math.pi) * s)
    right = math.exp(-math.pow(x - m, 2) / (2 * math.pow(s, 2)))
    return left * right


def showfigure():
    plt.figure(figsize=((8, 6)))  # 设置画布大小
    x = np.arange(-4, 5, 0.1)  # 绘制x（-4,5）
    y = []
    for i in x:
        y.append(gd(i, 0, 1))  # m为0，s为1
    plt.plot(x, y)
    plt.xlim(-4.0, 5.0)
    plt.ylim(-0.2, 0.5)
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

    # 设置并添加标签
    label_f1 = "$\mu=0,\ \sigma=1$"
    plt.text(2.5, 0.4, label_f1, fontsize=15, verticalalignment="top",
             horizontalalignment="left")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    label_f2 = r"正态分布函数 $f(x)=\frac{1}{\sqrt{2\pi}\sigma}exp(-\frac{(x-\mu)^2}{2\sigma^2})$"
    plt.text(0.5, 0.5, label_f2, fontsize=15, verticalalignment="top"
             , horizontalalignment="left")
    plt.show()


def main():
    showfigure()
    gd()


main()
