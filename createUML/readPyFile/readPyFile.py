# !/usr/bin/python
# -*- coding: UTF-8 -*-
from createUML.readPyFile.GetInformation import GetInformation

f = open('./GetInformation.py', 'r')
result=[]
for line in f:
    if line == '\n': continue
    else: result.append(line)
for i in result:
    i = i[0:len(i)-1]
    # print(i, '----')
    if (i[0:3] == 'def'):
        v3, funcModel = GetInformation().getClassFunction(i)
        if v3 == 1:
            print(funcModel.funcName)
            print(funcModel.returnValueType)
            print(funcModel.funcName)
    elif i[0:5] == 'class':
        v1, s1 = GetInformation().getClassName(i)
        if v1 == 1:
            print(s1)
    else:
        v2, methodModel = GetInformation().getClassMethod(i)
        if v2 == 1:
            print(methodModel.name)
            print(methodModel.type)

