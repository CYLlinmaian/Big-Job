'''
Author: CYLlinmaian
Date: 2022-07-10 12:07:53
LastEditTime: 2022-07-10 12:18:24
LastEditors: CYLlinmaian
Description: 
FilePath: \Big Job\Appearance Statistics.py
Copyright © 1999 - 2022 Mr.chen.All Rights Reserved.
'''
# CalThreeKingdoms.py
import jieba

# 创建删除词语集合
del_words = ["将军", "却说", "二人", "不可", "荆州", "不能", "如此", "商议", "如何",
             "主公", "军士", "左右", "军马", "引兵", "次日", "大喜", "天下", "于是", "东吴", "今日",
             "不敢", "魏兵", "陛下", "人马", "不知", "一人", "都督", "汉中"]
# 打开txt文件并且读取全部文本
file = open("三国演义.txt", "r+", encoding='utf-8').read()
# jieba精确模式分词，返回列表words
words = jieba.lcut(file)
dict_counts = {}
for word in words:
    if len(word) == 1:  # 排除单一字符如“的/地/也“的干扰
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德曰" or word == "玄德":
        rword = "刘备"
    elif word == "丞相" or word == "孟德":
        rword = "曹操"
    else:
        rword = word
    dict_counts[rword] = dict_counts.get(rword, 0) + 1
for i in del_words:
    del dict_counts[i]
items = list(dict_counts.items())

# 按出场次数降序排序
items.sort(key=lambda x: x[1], reverse=True)

for i in range(10):  # top10前十名
    word, count = items[i]
    print("人物：{0:<10}出场次数：{1:>5}".format(word, count))
