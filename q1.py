# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 13:44:02 2019

@author: lisa_
"""

filehandle = open("qbdata.txt","r")

Namel = []
Scorel = []
for i in filehandle.readlines():
    s = i[-5:-1]
    if s[0] == " ":
        s = s[1:]
    
    n = eval(s)
    Scorel.append(n)

    for o in range(len(i)):
        if i[o] == "Q":
            Namel.append(i[:o])

for p in range(len(Namel)):
    if Scorel[p] >= 60:
        print(Namel[p] + "has a rating of " + str(Scorel[p]))
filehandle.close()

