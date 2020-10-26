import numpy as np
import cv2
import matplotlib.pyplot as plt


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
rr = np.array(newImgR)

newImgTR = []
f = open("tr.txt","r")
lines = f.readlines()#读取全部内容
for line in lines:
    numbers = line.split(' ')
    intN = []
    for value in numbers:
        if value == '\n':
            continue;
        intN.append(int(value))
    newImgTR.append(intN)
tr = np.array(newImgTR)

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

tr = tr.reshape(270 * 464)
rr = rr.reshape(270 * 464)
gg = gg.reshape(270 * 464)
bb = bb.reshape(270 * 464)

newImgI = []
for (i1, i2, i3) in zip(rr, gg, bb):
    list = []
    list.append(i1)
    list.append(i2)
    list.append(i3)
    newImgI.append(list)

newImgI = np.array(newImgI)
newImgI = newImgI.reshape(270, 464, 3)
print(newImgI.shape)


newImgII = []
for (i1, i2, i3) in zip(tr, gg, bb):
    list = []
    list.append(i1)
    list.append(i2)
    list.append(i3)
    newImgII.append(list)

newImgII = np.array(newImgII)
newImgII = newImgII.reshape(270, 464, 3)
print(newImgII.shape)

plt.figure(figsize=(20,9),dpi=100)
plt.subplot(1,2,1)
plt.title("ord File")
plt.imshow(newImgI)

plt.subplot(1,2,2)
plt.title("new File")
plt.imshow(newImgII)
plt.show()

cv2.imwrite("filenameI.png", newImgI)

cv2.imwrite("filenameII.png", newImgII)



