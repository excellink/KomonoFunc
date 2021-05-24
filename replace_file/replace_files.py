# -*- coding: utf-8 -*-
# replace_files
# 功能：用于批量复制替换产生的同名文件
# 使用说明：将需要拷贝和替换的文件名写入copylist.txt中，每一行放一组用","分隔
#		如：file,file

import os
import shutil

f = open(r'D:/copylist.txt','r')
for line in f.readlines():
	src,dst = line.strip().split(",")
	path_src = os.path.join(r"E:/source/generated", src)
	path_dst = os.path.join(r"E:/source", dst)
	print(path_src + " ----> " + path_dst)
	shutil.copyfile(path_src,path_dst)
	print("------------------------------")
print("Finish")
f.close()
