# 私有属性与方法（Private Attributes & Methods）
# 使用双下划线 __ 前缀命名实现“伪私有”
# 有些属性或方法不希望被类外部访问或修改，希望“隐藏”起来，只能由类的内部代码访问
class MyClass:
    def __init__(self):
        self.__secret = "这是一个私有属性"

    def __hidden(self):
        print("这是一个私有方法")

    def public_method(self):
        print("这是一个公开方法")
        print("访问私有属性：", self.__secret)
        self.__hidden()

obj = MyClass()
obj.public_method()    # ✅ 正常调用

# print(obj.__secret)    # ❌ 报错：AttributeError
# AttributeError: 'MyClass' object has no attribute '__secret'

# obj.__hidden()         # ❌ 报错：AttributeError
# AttributeError: 'MyClass' object has no attribute '__hidden'
print('-' * 40)


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # 私有属性

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("❌ 余额不足")

    def show_balance(self):
        print(f"{self.owner} 的余额是：{self.__balance} 元")

acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.show_balance()

print(acc.__balance)                # ❌ 报错
print(acc._BankAccount__balance)    # ✅ 访问私有属性（不推荐）


