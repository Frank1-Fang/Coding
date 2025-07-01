# ======================================================
# Python 模块（Module）基础笔记（适合写入 .py 文件学习）
# ======================================================
# 一、什么是模块？
# 模块（Module）是一个 .py 文件，里面包含变量、函数、类等定义。
# 本质上就是一个“功能文件”，可被其他 Python 文件导入使用，实现代码复用。

# 示例：mymath.py
# def add(a, b):
#     return a + b

# 二、模块的好处
# 1. 代码复用：定义一次，导入多次使用
# 2. 命名空间隔离：不同模块中同名变量/函数不会冲突
# 3. 项目结构清晰：每个功能一个模块，便于协作与维护

# 三、模块的使用方式（导入）

# 1. import 模块名（推荐）
# import math
# print(math.sqrt(16))

# 2. from 模块 import 函数名
# from math import sqrt
# print(sqrt(25))

# 3. from 模块 import * （不推荐，容易变量冲突）
# from math import *
# print(sin(pi / 2))

# 4. import 模块 as 别名
# import math as m
# print(m.sqrt(9))

import mymath

print("加法结果：", mymath.add(2, 3))        # 输出 5
print("乘法结果：", mymath.multiply(4, 5))   # 输出 20
print("圆周率：", mymath.PI)

from mymath import add as my_add
print("加法结果：", my_add(100, 200))

import mymath as mm
print("乘法结果：", mm.add(200, 300))

# dir() 函数: 内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
# >>> import mymath
# >>> dir(mymath)
# ['PI', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
# '__name__', '__package__', '__spec__', 'add', 'multiply']
# 可以找到我们自己在mymath.py中定义的变量 PI 和函数 add, multiply


