import os
filePath = '/Users/liupeng/PycharmProjects/PythonTools/setBlog/_posts/'
newFilePath = '/Users/liupeng/PycharmProjects/PythonTools/setBlog/post/'
fileNameList = []
for i,j,k in os.walk(filePath):
    fileNameList = k
k = 0
for ii in fileNameList:
    f = open(filePath + ii)
    name = newFilePath + ii
    name = name[0:len(name)-2] + 'markdown'
    file2 = open(name, 'w+', encoding='utf-8')
    line = f.readline()  # 调用文件的 readline()方法
    print("正在标准化: 《" + str(ii) + "》\n")
    i = 0
    while line:
        if i == 0:
            file2.write('---\n')
        elif i == 1:
            file2.write('layout: post\n')                                           # layout
        elif i == 2:
            categories = line
        elif i == 3:
            title = line[6:len(line)-1]
            file2.write('title: "' + title + '"\n')                                                       # title
            file2.write('date: ' + ii[0:10] + ' 20:30:00 + 0800' + '\n')            # data
        elif i == 4:
            pass
        elif i == 5:
            file2.write('categories: technology\n')                                 # categories
        elif i == 6:
            tag = line[7:len(line)-2]
            # tags: [keras]
            file2.write('tags: ' + tag + '\n')                                                       # tags
        elif i == 7:
            if k % 2 == 0:
                file2.write('img: https://ae03.alicdn.com/kf/Hb7f0c7d7d5844015954e4ea058d9d6710.png\n') # img
                k = k + 1
            else:
                file2.write('img: https://ae02.alicdn.com/kf/H9378f2d8036b406a90d8eed979c1684fD.png\n')
                k = k + 1
        elif i == 8:
            file2.write('---\n')
        else:
            file2.write(line)
        i = i + 1
        line = f.readline()
    f.close()
    file2.close()
    print("标准化: 《" + str(ii) + "》>完成✅\n")