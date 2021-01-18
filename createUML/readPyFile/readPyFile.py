# !/usr/bin/python
# -*- coding: UTF-8 -*-

f = open('../../KnightsOfTheApocalypse/lpFunction.py', 'r')
result=[]
for line in f:
	result.append(line)
for i in result:
    print(i, end='')
