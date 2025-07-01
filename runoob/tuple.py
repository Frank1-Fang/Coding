print("Python Tuple 元组")

# 创建元组
t = (10, 20, 30, 40, 50)
print("原始元组：", t)

# 访问元素
print("t[0] =", t[0])
print("t[-1] =", t[-1])  # 最后一个元素

# 切片
print("t[1:4] =", t[1:4])

# 拼接
t2 = (60, 70)
print("拼接后的元组：", t + t2)

# 重复
print("重复两次：", t * 2)

# 成员检查
print("30 是否在 t 中？", 30 in t)

# 遍历
for val in t:
    print("遍历元素：", val)

# 嵌套元组
nested = (1, [2, 3], (4, 5))
print("嵌套元组：", nested)
print("访问内部列表元素：", nested[1][1])
print("访问内部元组元素：", nested[2][0])
