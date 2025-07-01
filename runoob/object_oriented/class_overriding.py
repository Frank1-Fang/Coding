# 继承与方法重写（Inheritance & Method Overriding）
# 继承（Inheritance）是指一个类可以“继承”另一个类的属性和方法。
# 被继承的类叫做 父类 / 基类（Base Class / Superclass）
# 继承的类叫做 子类 / 派生类（Subclass / Derived Class）

# 基本语法：
"""
class Parent:
    # 父类内容

class Child(Parent):
    # 子类内容（可重写、可新增）
"""

# 1. 子类继承父类
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"你好，我是 {self.name}")

# Student 继承 Person
class Student(Person):
    def study(self):
        print(f"{self.name} 正在学习 Python")

stu = Student("小明")
stu.say_hello()  # 来自父类
stu.study()      # 来自子类
print('-' * 40)

# 2. 方法重写（Override）
# 子类可以“重写”父类的方法，使其具有不同的行为
class Person:
    def say_hello(self):
        print("你好，我是人类")

class Student(Person):
    def say_hello(self):  # 重写父类方法
        print("你好，我是学生")

p = Person()
s = Student()

p.say_hello()  # 输出：你好，我是人类
s.say_hello()  # 输出：你好，我是学生
print('-' * 40)

# 3. 使用 super() 调用父类方法
# super() 是一个内置函数，用于调用父类的方法，尤其常见于重写 __init__() 时
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)  # 调用父类构造器
        self.grade = grade

    def info(self):
        print(f"{self.name} 读 {self.grade} 年级")

s = Student("小红", 3)
s.info()
print('-' * 40)

# 4. 子类扩展属性或方法
# 子类不仅可以重写方法，还可以添加新的属性和方法
class Animal:
    def move(self):
        print("动物会动")

class Bird(Animal):
    def fly(self):
        print("鸟会飞")

b = Bird()
b.move()  # 来自 Animal
b.fly()   # 来自 Bird





