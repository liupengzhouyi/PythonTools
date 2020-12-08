import random
import numpy
import cv2
from PIL import Image


def getOneList():
    list = [0, 0, 0, 0, 0, 0, 0]
    number = random.randint(1, 7)
    for i in range(number):
        tempIndex = random.randint(1, 100)
        list[tempIndex%7-1] = 1
    return list

a = getOneList()
b = getOneList()
c = getOneList()
d = getOneList()

image = []

image.append(a)
image.append(b)
image.append(c)
image.append(d)
image.append(c)
image.append(b)
image.append(a)

a1 = []
a2 = []
a3 = []
a4 = []
a5 = []
a6 = []
a7 = []
index = 0

for i in image:
    a1.append(i[0])
    a2.append(i[1])
    a3.append(i[2])
    a4.append(i[3])
    a5.append(i[4])
    a6.append(i[5])
    a7.append(i[6])
    index = index + 1

p = []
p.append(a1)
p.append(a2)
p.append(a3)
p.append(a4)
p.append(a5)
p.append(a6)
p.append(a7)

for i in p:
    print(i)



from matplotlib import pyplot as plt
import matplotlib as mpl
plt.figure(figsize=(6, 6))

c1 = random.randint(0, 999)
c2 = random.randint(0, 999)
c3 = random.randint(0, 999)

o1 = ''
if len(str(c1%99)) == 1:
    o1 = '0' + str(c1%99)
else:
    o1 = str(c1 % 99)

o2 = ''
if len(str(c2%99)) == 1:
    o2 = '0' + str(c2%99)
else:
    o2 = str(c2 % 99)

o3 = ''
if len(str(c3%99)) == 1:
    o3 = '0' + str(c3%99)
else:
    o3 = str(c3 % 99)

color = str('#') + o1 + o2 + o3

colors = ['w', color]
cmap = mpl.colors.ListedColormap(colors)

plt.axis('off')
plt.imshow(numpy.array(p), interpolation='nearest', cmap=cmap)
plt.savefig("filename.png", dpi=150)
plt.show()





