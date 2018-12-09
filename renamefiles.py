# -*- coding: utf-8 -*-
# rename_files
# 功能：统一修改文件名，保持原文件类型不变，若非文件则不进行修改
# version 0.1 获取文件名称 version 0.2.1 更改文件名称
# version 0.2.2 更改文件名称并保留文件原来格式后缀
import os


def rename_files(file_path):
    files = os.listdir(file_path)   # 取出file_path地址中的所有文件/文件夹名组成list
    n = 0   # 计数变量
    print("请输入所需更改的文件名：")
    str_name = input()
    for file in files:
        file_dir = os.path.join(file_path, file)
        if os.path.isdir(file_dir):
            continue
        else:                       # 否则就连起来打印
            file_dir = os.path.join(file_path, file)    # 连接file路径和名字
            f_name, fe_name = os.path.splitext(file_dir)    # 拆分路径文件名与后缀
            new_name = os.path.join(file_path, str_name + str(n)) + fe_name
            # os.rename(file_dir, new_name)
            n = n+1
            print(file_dir, "=====>", new_name)


filepath = 'D:\\test'

rename_files(filepath)


