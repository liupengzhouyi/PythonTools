import cv2
import numpy as np
from matplotlib import pyplot as plt

pic_file = 'ordFile.jpeg'

img_bgr = cv2.imread(pic_file, cv2.IMREAD_COLOR) #OpenCV读取颜色顺序：BRG
img_b = img_bgr[..., 0]
img_g = img_bgr[..., 1]
img_r = img_bgr[..., 2]
fig = plt.gcf()                                  #图片详细信息


fig = plt.gcf()                                  #分通道显示图片
fig.set_size_inches(10, 15)

plt.subplot(221)
plt.imshow(np.flip(img_bgr, axis=2))             #展平图像数组并显示
plt.axis('off')
plt.title('Image')

plt.subplot(222)
plt.imshow(img_r, cmap='gray')
plt.axis('off')
plt.title('R')

plt.subplot(223)
plt.imshow(img_g, cmap='gray')
plt.axis('off')
plt.title('G')

plt.subplot(224)
plt.imshow(img_b, cmap='gray')
plt.axis('off')
plt.title('B')

plt.show()


information = "zbcdeftcfvygbuhinjtfyvgubhirdtygbuhinjtcfyvgubhi" \
			  "tfyguhijtfyvgubhijtcfyvgubhinjmktryuyuhiebvauhbk" \
			  "yguhijtfyvgubhijtcfyvgubhinjmktryuyuhiebvauhbkgg" \
			  "yguhijtfyvgubhijtcfyvgubhinjmktryuyuhiebvauhbkfg" \
			  "yguhijtfyvgubhijtcfyvgubhinjmktryuyuhiebvauhbkkk" \
			  "yguhijtfyvgubhijtcfyvgubhinjmktryuyuhiebvauhbkjj######"
informationII = []
for char in information:
	informationII.append(ord(char))


length = len(informationII)
index = 0
print(img_r.shape)
# 追加后，打开并读取该文件：
f = open("r.txt", "w+")
f1 = open('tr.txt', 'w+')
for l in img_r:
	for r in l:
		f.write(str(int(r)) + ' ')
		if index < length:
			if int(r) <= 128:
				f1.write(str(int(r) + informationII[index]) + ' ')
			else:
				f1.write(str(int(r) - informationII[index]) + ' ')
		else:
			f1.write(str(int(r)) + ' ')
		index = index + 1
	f.write('\n')
	f1.write('\n')
f.close()

f = open("g.txt", "w+")
for l in img_g:
	for r in l:
		f.write(str(int(r)) + ' ')
	f.write('\n')
f.close()

f = open("b.txt", "w+")
for l in img_b:
	for r in l:
		f.write(str(int(r)) + ' ')
	f.write('\n')
f.close()






