# __init__() 是 Python 中的构造方法（constructor），当你创建类的实例时，它会被自动调用
# 常用来给对象设置初始属性值（即定义实例变量）
# 实例变量是每个对象独立拥有的属性，通常在 __init__() 里通过 self.xxx 方式定义
# 与类属性（ClassName.xxx）不同，实例变量属于具体的对象实例，彼此之间互不影响
# 语法结构
"""
class ClassName:
    def __init__(self, 参数1, 参数2, ...):
        # self.属性1 = 参数1
        # self.属性2 = 参数2
"""

class Complex:
    def __init__(self, real, imag):
        self.r = real      # 实例变量 r (给实例对象设置属性)
        self.i = imag      # 实例变量 i

# 创建对象
x = Complex(3.0, -4.5)

# 访问实例变量
print("实部：", x.r)     # 输出：3.0
print("虚部：", x.i)     # 输出：-4.5

# 多个对象互不影响
a = Complex(1, 2)
b = Complex(5, 6)

a.r = 10
print("a 的实部：", a.r)  # 10
print("b 的实部：", b.r)  # 5 （没有改变）
print('-' * 40)
# 默认值 & 关键字参数
class Person:
    def __init__(self, name="匿名", age=18): # 为 name 设置默认值 "匿名"
        self.name = name
        self.age = age

p1 = Person()
p2 = Person("Alice", 25)

print(p1.name, p1.age)  # 匿名 18
print(p2.name, p2.age)  # Alice 25
print('-' * 40)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("Python入门", "张三")
book2 = Book("AI实战", "李四")

print(book1.title, "-", book1.author)
print(book2.title, "-", book2.author)