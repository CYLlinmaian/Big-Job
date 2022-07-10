'''
Author: CYLlinmaian
Date: 2022-07-10 12:07:48
LastEditTime: 2022-07-10 12:15:04
LastEditors: CYLlinmaian
Description: 
FilePath: \Big Job\Reverse a string.py
Copyright © 1999 - 2022 Mr.chen.All Rights Reserved.
'''
def strReverse(strDemo):
    strList = []  # 构造列表
    print("陈勇林——201905054103")
    for i in range(len(strDemo) - 1, -1, -1):  # 循环遍历字符串
        strList.append(strDemo[i])  # 从后往前添加元素
    return "".join(strList)


print(strReverse("!nam emosdnah a si nilgnoynehC"))
