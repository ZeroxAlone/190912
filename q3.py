# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:41:43 2019

@author: lisa_
"""

import jieba
txt = open("三国演义.txt", "r", encoding = "utf -8" ).read()

words = jieba.lcut(txt)
excludes = {"将军","却说","二人","不可","荆州","不能","如此","商议",
            "如何","主公","军士","左右","军马","引兵","次日","大喜","天下",
            "东吴","于是","今日","16","不敢","魏兵","陛下","人马","都督","一人","不知","汉中",
            "众将","只见","后主","兵","大叫","上马","此人","先主","太守","天子","后人","背后",
            "一面","城中","何不","忽报","大军","先生","何故","然后","先锋","夫人","不如"}

counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "孔明" or word == "孔明曰":
        rword = "诸葛亮"
    elif word =="关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德日": 
        rword = "张飞"
    elif word == "孟德" or word == "丞相" or word == "丞相日" or word == "曹孟德":
        rword ="曹操"
    else:
        rword = word
counts[rword] = counts. get(rword, 0) + 1

for i in excludes:
    del counts[i]

listhills = list(counts. items()) 
listhills. sort(key=lambda x:x[1], reverse=True)

for k in range(15):
    word, counts = listhills[k]
    print("{0:<10}{1:>5}". format(word, counts))