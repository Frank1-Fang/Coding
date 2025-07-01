# 运算符重载（Operator Overloading）
# Python 允许我们自定义类中运算符的行为，这就叫做“运算符重载”
# 提高代码可读性、可维护性，让自定义类的对象像内建类型一样自然运算
print("Overload '+'")
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # 重载 +
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):  # 打印对象
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 1)
v3 = v1 + v2      # 实际调用 v1.__add__(v2)
print(v3)         # 输出：Vector(6, 4)
print('-' * 40)

print("Overload '>'")
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __gt__(self, other):  # 大于比较
        return self.score > other.score

s1 = Student("Alice", 85)
s2 = Student("Bob", 78)

print(s1 > s2)  # True，调用 s1.__gt__(s2)
print('-' * 40)

print("Overload '/'")
class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __truediv__(self, other):
        return Fraction(self.num * other.den, self.den * other.num)

    def __repr__(self):
        return f"{self.num}/{self.den}"

f1 = Fraction(1, 2)
f2 = Fraction(2, 3)
print(f1 / f2)  # 输出：3/4

#| 运算符  |      方法名       | 示例用法 |
#| ------- | ----------------- | -------- |
#| `+`     | `__add__`         | `a + b`  |
#| `-`     | `__sub__`         | `a - b`  |
#| `*`     |   `__mul__`       | `a * b`  |
#| `/`     | `__truediv__`     | `a / b`  |
#| `//`    | `__floordiv__`    | `a // b` |
#| `%`     | `__mod__`         | `a % b`  |
#| `**`    | `__pow__`         | `a ** b` |
#| `==`    | `__eq__`          | `a == b` |
#| `!=`    | `__ne__`          | `a != b` |
#| `<`     | `__lt__`          | `a < b`  |
#| `>`     | `__gt__`          | `a > b`  |
#| `<=`    | `__le__`          | `a <= b` |
#| `>=`    | `__ge__`          | `a >= b` |
