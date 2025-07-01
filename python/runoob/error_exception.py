# ===================================================
# 📘 Python 常见 10 类异常（异常类型 + 示例 + 注释）
# ===================================================

# 1. ZeroDivisionError：除以 0
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError：不能除以 0")

# 2. ValueError：类型转换失败（如 str → int）
try:
    num = int("abc")  # 字符串不能转换为整数
except ValueError as e:
    print("ValueError：不能将字符串转换为整数")

# 3. TypeError：类型不匹配操作
try:
    result = "2" + 3  # 字符串 + 整数
except TypeError as e:
    print("TypeError：类型不匹配，不能拼接 str 和 int")

# 4. NameError：使用未定义变量
try:
    print(unknown_variable)
except NameError as e:
    print("NameError：变量未定义")

# 5. IndexError：访问列表越界
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError as e:
    print("IndexError：列表索引超出范围")

# 6. KeyError：访问字典中不存在的键
try:
    d = {"a": 1, "b": 2}
    print(d["c"])
except KeyError as e:
    print("KeyError：访问了不存在的字典键")

# 7. FileNotFoundError：文件未找到
try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print("FileNotFoundError：文件不存在")

# 8. AttributeError：访问不存在的对象属性或方法
try:
    s = "hello"
    s.push("x")  # 字符串没有 push 方法
except AttributeError as e:
    print("AttributeError：对象没有该属性或方法")

# 9. ImportError：导入模块失败（模块不存在或拼写错误）
try:
    import non_existing_module
except ImportError as e:
    print("ImportError：导入模块失败")

# 10. IndentationError：缩进错误（仅在语法阶段出现，无法通过 try 捕获）
# ❌ 注意：IndentationError 是语法错误，不能用 try-except 捕获
# 示例（运行此行会直接报错，建议注释掉）：
# def func():
# print("缩进错误")  # 缺少缩进