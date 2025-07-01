# self 是指向实例对象本身的变量
# 类的方法第一个参数必须是 self
# 当你通过对象调用方法时，Python 会自动把这个对象作为第一个参数传入 self
# self.xxx 表示“该对象自己的属性或方法”

class Student:
    def set_name(self, name):   # self 代表调用该方法的对象
        self.name = name        # 给实例设置一个 name 属性

    def greet(self):
        print("你好，我是", self.name)

# 创建对象
stu1 = Student()
stu1.set_name("Alice")  # 实际调用：Student.set_name(stu1, "Alice")
stu1.greet()            # 实际调用：Student.greet(stu1)
print('-' * 40)

# self 可访问对象自己的所有变量 & 方法
class Counter:
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1
        self.show()

    def show(self):
        print("当前计数：", self.count)

c = Counter()
c.increase()  # 输出：当前计数：1
c.increase()  # 输出：当前计数：2
