# 1. 实例方法（Instance Method）
# 第一个参数是 self，代表对象本身，可访问和修改实例属性
class Dog:
    def bark(self):  # 实例方法
        print("Dog: Wang Wang Wang!")

dog = Dog()
dog.bark()  # 实际是 Dog.bark(dog)
print('-' * 40)

# 2. 类方法（Class Method）
# 用 @classmethod 装饰，第一个参数是 cls，代表类本身
# 常用于构建类级别的数据，或作为“构造器辅助方法”
class Person:
    species = "人类"

    @classmethod
    def describe_species(cls):
        print("我们是", cls.species)

Person.describe_species()  # ✅ 类调用
p = Person()
p.describe_species()       # ✅ 实例也可调用
print('-' * 40)

# 3. 静态方法（Static Method）
# 用 @staticmethod 装饰，没有 self 或 cls 参数
# 不能访问实例或类属性，只是放在类中的一个普通函数
class MathTool:
    @staticmethod
    def add(a, b):
        return a + b

print(MathTool.add(3, 4))  # 输出：7
print('-' * 40)

# 综合例子
class Student:
    school = "Python高校"

    def __init__(self, name):
        self.name = name

    def show(self):               # 实例方法
        print(f"{self.name} 来自 {self.school}")

    @classmethod
    def get_school(cls):          # 类方法
        print(f"学校是：{cls.school}")

    @staticmethod
    def greet():                  # 静态方法
        print("欢迎使用 Python 学习系统！")

# 测试
stu = Student("Alice")
stu.show()            # 实例方法
Student.get_school()  # 类方法
Student.greet()       # 静态方法

