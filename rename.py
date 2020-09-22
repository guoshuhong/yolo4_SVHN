import os
#输入文件位置，注意实现双斜杠
path = "mchar_val"
#该文件夹下所有的文件
filelist = os.listdir(path)

for file in filelist:   #遍历所有文件
    Olddir=os.path.join(path,file)   #原来的文件路径
    if os.path.isdir(Olddir):   #如果是文件夹则跳过
        continue
    filename=os.path.splitext(file)[0]   #文件名
    filetype=os.path.splitext(file)[1]   #文件扩展名
    num = int(filename)
    nums = str(num)
    Len  = 6 - len(nums)
    Newdir=os.path.join(path, "0" + str(num)+filetype)  #用字符串函数zfill 以0补全所需位数
    os.rename(Olddir,Newdir)#重命名
