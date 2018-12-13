# -*- coding: utf-8 -*-
# rename_files
# 功能：统一修改文件名，保持原文件类型不变，若非文件则不进行修改
import os


def rename_files(f_tuple):
    n = 0   # 计数变量
    print("请输入所需更改的文件名：")
    str_name = input()
    for t in f_tuple:
        f_dir = t[0]
        f_name, fe_name = os.path.splitext(f_dir)    # 拆分路径文件名与后缀
        new_name = os.path.join(os.path.dirname(t[0]), str_name + str(n)) + fe_name
        os.rename(f_dir, new_name)
        n = n+1
        print(f_dir, "---->", new_name)


def createdict(file_path) -> tuple:
    files = os.listdir(file_path)   # 取出file_path地址中的所有文件/文件夹名组成list
    f_key = []
    f_value = []
    for file in files:
        file_dir = os.path.join(file_path, file)
        if os.path.isdir(file_dir):
            continue
        else:
            file_dir = os.path.join(file_path, file)  # 连接file路径和名字
            f_size = os.path.getsize(os.path.join(file_path, file))  # 获取大小
            f_key.append(file_dir)
            f_value.append(f_size)
    f_tuple = dict(zip(f_key, f_value))
    f_tuple_sorted = sorted(f_tuple.items(), key=lambda x: x[1])
    return f_tuple_sorted


filepath = 'D:\\test'
temp = createdict(filepath)
rename_files(temp)