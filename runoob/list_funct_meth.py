print("Python 列表函数 & 方法完整示例")
# Python 中 函数（function） 和 方法（method）的区别
# 函数（function）：一个独立的可调用代码块，用于执行特定任务，可以作用于任意对象
# 使用方法：function(obj)
# 通用性：可以操作任意类型

# 方法（method）：附属于某个对象（如列表、字符串等）的函数，是对象的一部分
# 使用方法：obj.method()
# 通用性：只能作用于特定类型（如列表、字符串）

# 创建一个列表
my_list = [3, 1, 4, 1, 5]
print("初始列表：", my_list)

# 1. len()
print("长度 len():", len(my_list))  # 5

# 2. max(), min()
print("最大值 max():", max(my_list))  # 5
print("最小值 min():", min(my_list))  # 1

# 3. list() 把元组转换成列表
t = (6, 7)
converted = list(t)
print("元组转换为列表 list((6,7)):", converted)

# 4. append()
my_list.append(9)
print("append(9): ", my_list)

# 5. count(1)
print("count(1): ", my_list.count(1))  # 2

# 6. extend()
my_list.extend([2, 6])
print("extend([2,6]): ", my_list)

# 7. index()
print("index(4): ", my_list.index(4))  # 返回第一次出现4的位置

# 8. insert()
my_list.insert(2, 100)
print("insert(2,100): ", my_list)

# 9. pop()
last = my_list.pop()
print("pop() 弹出元素: ", last)
print("当前列表：", my_list)

# 10. remove()
my_list.remove(1)  # 移除第一次出现的1
print("remove(1): ", my_list)

# 11. reverse()
my_list.reverse()
print("reverse() 反转: ", my_list)

# 12. sort()
my_list.sort()
print("sort() 排序: ", my_list)

# 13. copy()
copied = my_list.copy()
print("copy() 复制的新列表: ", copied)

# 14. clear()
my_list.clear()
print("clear() 清空后: ", my_list)
