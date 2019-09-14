# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:41:42 2019

@author: lisa_
"""

filehandle = open("hamlet.txt","r") 
t = filehandle.read()
for u in "!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\":
    t = t.replace(u, " ")
wds = t.split()
c = {}
for i in wds:
    c[i] = c.get(i,0) + 1

file = open("freqofham.txt","w")

for o in c:
    f = "{}:{}".format(o,c[o])
    n= file.write(f.lower() + "\n")

file.close()
filehandle.close()