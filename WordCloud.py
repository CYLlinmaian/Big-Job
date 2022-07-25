'''
Author: CYLlinmaian
Date: 2022-07-10 12:07:46
LastEditTime: 2022-07-25 11:10:09
LastEditors: CYLlinmaian
Description: 
FilePath: \Big Job\WordCloud.py
Copyright © 1999 - 2022 Mr.chen.All Rights Reserved.
'''

import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud


def trans_ch(txt):
    words = jieba.lcut(txt)
    newtxt = ''.join(words)
    return newtxt


f = open('abouty.txt', 'r', encoding='utf-8')
txt = f.read()
f.close
txt = trans_ch(txt)
mask = np.array(Image.open("abouty.png"))  # 将你的背景图片
wordcloud = WordCloud(background_color="white",  # 设置词云背景
                      width=800,
                      height=600,
                      max_words=200,
                      max_font_size=100,
                      mask=mask,
                      contour_width=4,
                      contour_color='steelblue',
                      font_path="STLITI.ttf"  # 指定字体
                      ).generate(txt)
wordcloud.to_file('abouty.png')
