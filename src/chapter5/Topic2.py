#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python3.9 
@File    ：Topic2.py.py
@Author  ：lxy(2305195328@qq.com)
@Date    ：2023/3/5 14:38 
"""

"""
用import math as mymath 导入math库，要使用其中的sqrt()函数，正确的调用方式是()、
A. math.sqrt(3)     B. sqrt(3)
C. mymath.sqrt(3)   C. math.mymath.sqrt(3)
"""

"""
答案：C，导入了整个模块math调用函数时要用模块名.函数名
但是这里math模块别名为mymath，所以调用函数为别名.函数名
"""