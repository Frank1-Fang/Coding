def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

PI = 3.14159

if __name__ == "__main__":
    print("当前运行的是 mymath.py，本模块被直接执行！")
    print("测试 add(2, 3) =", add(2, 3))        # 输出 5
    print("测试 multiply(4, 5) =", multiply(4, 5))  # 输出 20
else:
    print("mymath 模块已被导入，__name__ =", __name__)

# 加上 if __name__ == "__main__": 是让模块既能独立运行测试，又能被其他模块安全导入使用的标准写法。