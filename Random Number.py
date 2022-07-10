'''
Author: CYLlinmaian
Date: 2022-07-10 12:07:49
LastEditTime: 2022-07-10 12:15:43
LastEditors: CYLlinmaian
Description: 
FilePath: \Big Job\Random Number.py
Copyright © 1999 - 2022 Mr.chen.All Rights Reserved.
'''
import random

print("陈勇林——201905054103")
print("6位随机数为：")


def creatrandomcode():
    res1 = ""  # 创建变量res1用于存放随机生成的数字
    res2 = ""  # 创建变量res2用于存放随机生成的大写英文字母
    res3 = ""  # 创建变量res3用于存放随机生成的小写英文字母
    for i in range(2):  # 使用循环语句，控制随机选择数字、字母的次数，修改随机生成每字母（数字）的次数可以控制验证码的长度
        num = random.randint(0, 9)  # 创建变量num,用于存放从0到9之间随机抽取的数字
        res1 += str(num)  # 将两次随机生成的数字连接起来
        # 创建变量num,用于存放大写字母A到Z之间随机抽取的数字，大写字母的十进制范围是（65,91）
        num = random.randint(65, 91)
        res2 += str(chr(num))
        # 创建变量num,用于存放大写字母A到Z之间随机抽取的数字，大写字母的十进制范围是（65,91），小写字母的十进制范围是（97,123）
        num = random.randint(97, 123)
        res3 += str(chr(num))
    string = str(res1 + res2 + res3)
    print(string)


creatrandomcode()

