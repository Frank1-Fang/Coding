# 定义一个类
# 基本语法
"""
class ClassName:
    # 类属性（可选）
    # 方法定义
    def method_name(self):
        pass
"""

class MyClass:
    i = 12345  # 类属性，所有实例共享

    def f(self):  # 实例方法（self一定要，并且必须作为第一个参数！）
        return "Hello, world!"

# 实例化类，创建对象
x = MyClass()

# 访问类属性
print("属性 i 的值是：", x.i)

# 调用实例方法
print("调用 f() 方法返回：", x.f())
print('-' * 40)

# i = 12345 是类属性，不依赖对象，是所有对象共享的
# def f(self) 是实例方法，通过 x.f() 来调用；
# x = MyClass() 创建了类的一个实例 x，这就像是“制造了一件产品”。

class Student:
    school = "Python高校"  # 类属性

    def greet(self):
        return "我是学生，很高兴学习 Python！"

stu = Student()
print(stu.school)
print(stu.greet())
