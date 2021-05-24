#!/usr/bin/python
# -*- coding: UTF-8 -*-
# ts_download
# 功能：下载ts文件

import os

# 打开配置文件 分别读取各行信息
# line[0] 地址
# line[1] 索引 + 文件名
# line[2] 格式
# line[3] 输出目录
config_path = os.path.join(os.getcwd(), "m3u8.txt")

f = open(config_path, 'r', encoding='utf-8')
line = f.readlines()
ts_addr = line[0].strip('\n')
print("----------------------------------------------------------")

output_name = line[1].strip('\n') + '.' + line[2].strip('\n') 
output_path = os.path.join(line[3].strip('\n'), output_name)
cmd = "ffmpeg -i " + ts_addr + " -c copy " + output_path
print(cmd)
os.system(cmd)
f.close()
