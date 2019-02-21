#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author:JiangM
# @Date:2018/9/12
import re

if __name__ == '__main__':
    str = 'hfgdf1233ffg45'
    pa = re.compile(r'[0-9]{4}')
    str2 = re.findall(pa, str)
    print(str2)

