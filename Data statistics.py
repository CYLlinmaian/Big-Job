'''
Author: CYLlinmaian
Date: 2022-07-10 12:07:53
LastEditTime: 2022-07-10 12:16:50
LastEditors: CYLlinmaian
Description: 
FilePath: \Big Job\Data statistics.py
Copyright © 1999 - 2022 Mr.chen.All Rights Reserved.
'''
print("陈勇林——201905054103")


def getNum():
    nums = []
    iNumStr = input("请输入数字: ")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字: ")
    return nums


def outputList(list):
    for i in range(len(list)):
        print(list[i])


def mean(numbers):
    s = 0.0
    for num in numbers:  # for语句表示列表中取出每一个元素
        s = s + num
    return s / len(numbers)  # len用于计算长度


def dev(numbers, mean):  # 计算标准差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean) ** 2
    return pow(sdev / (len(numbers) - 1), 0.5)


def median(numbers):  # 计算中位数
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size // 2 - 1] + numbers[size // 2]) / 2
    else:
        med = numbers[size // 2]
    return med


def findMax(list):  # 查找顺序最大的数字或字母
    num_max = list[0]
    for i in range(len(list)):
        if list[i] >= num_max:
            num_max = list[i]
    return num_max


def findMin(list):  # 查找顺序最小的数字或字母
    num_min = list[0]
    for i in range(len(list)):
        if list[i] <= num_min:
            num_min = list[i]
    return num_min


n = getNum()  # 将mean函数中的均值作为参数输入到标准差函数中
m = mean(n)
print("平均值:{:.2f},方差:{:.2f},中位数:{},最大值:{},最小值:{}".
      format(m, dev(n, m), median(n), findMax(n), findMin(n)))
