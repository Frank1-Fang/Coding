# ============== 处理用户键盘输入常用函数 ============== 
# 1. input()        → 读取一整行字符串
# 2. .split()       → 默认按空格分割为字符串列表 (.split(",") 则手动定义用逗号来分隔)
# 3. map(type, lst) → 将列表中每项转为指定类型（int/float）
# 4. list(...)      → 将 map 对象转成列表（可选）


# 1. 单个输入
x = input("请输入一个数字：")
print("你输入的是：", x)
print("-" * 40)

# 2. 多个输入（字符串分割）
# hello world → 输出 ['hello', 'world']
s = input("请输入两个单词，用空格分隔：")
words = s.split()
print("你输入的是：", words)
print("-" * 40)

# 3. 多个数字输入 + 转换为整数
s = input("请输入两个数字，用空格分隔：")
nums = s.split()  # ['3', '5']
a = int(nums[0])
b = int(nums[1])
print("相加结果：", a + b)
print("-" * 40)

# 4. 使用 map() 简化转换（经典写法）
a, b = map(int, input("请输入两个整数：").split())
print("相乘结果：", a * b)
print("-" * 40)

# 5. 处理任意多个输入数（列表形式）
nums = list(map(int, input("请输入若干整数：").split()))
print("输入整数列表：", nums)
print("-" * 40)

# 6. 输入用逗号分隔的数据
values = list(map(int, input("请输入数据（用逗号分隔）：").split(",")))
print("你输入的用逗号分隔后的数据: ", values)

