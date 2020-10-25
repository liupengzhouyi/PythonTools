import numpy as np

newImgR = []
f = open("tr.txt","r")
lines = f.readlines()#读取全部内容
for line in lines:
    numbers = line.split(' ')
    intN = []
    for value in numbers:
        if value == '\n':
            continue;
        intN.append(int(value))
    newImgR.append(intN)

print(newImgR)
print(np.array(newImgR).shape)

rr = np.array(newImgR)

newImgG = []
f = open("g.txt","r")
lines = f.readlines()#读取全部内容
for line in lines:
    numbers = line.split(' ')
    intN = []
    for value in numbers:
        if value == '\n':
            continue;
        intN.append(int(value))
    newImgG.append(intN)

gg = np.array(newImgG)

newImgB = []
f = open("b.txt","r")
lines = f.readlines()#读取全部内容
for line in lines:
    numbers = line.split(' ')
    intN = []
    for value in numbers:
        if value == '\n':
            continue;
        intN.append(int(value))
    newImgB.append(intN)

bb = np.array(newImgB)


rr = rr.reshape(270, 464)
gg = gg.reshape(270, 464)
bb = bb.reshape(270, 464)

newImg = np.array([rr, bb, gg])
newImg = newImg.reshape(270, 464, 3)

print(newImg.shape)

import cv2
import numpy as np
cv2.imwrite("filename.png", newImg)



