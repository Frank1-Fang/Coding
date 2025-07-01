# 1. try/except：基础异常捕获
# 捕获 ValueError 异常，防止程序因非法输入崩溃
try:
    x = int(input("请输入一个整数："))  # 若输入 'abc' 则抛出 ValueError
    print("你输入的是：", x)
except ValueError:
    print("❌ 输入无效，请输入整数！")

# 2. try/except...else：分支结构更清晰
# 打开文件：若成功 → 进入 else，失败 → except
try:
    f = open("sample.txt", "r")  # 如果文件不存在，会抛出 IOError
except IOError:
    print("❌ 文件打开失败，请检查文件是否存在")
else:
    print("✅ 文件打开成功，共有行数：", len(f.readlines()))
    f.close()  # 在 else 块中安全关闭文件

try:
    y = int(input("请输入一个整数："))  # 若输入 'abc' 则抛出 ValueError
    print("你输入的是：", y)
except ValueError:
    print("❌ 输入无效，请输入整数！")
else:
    print("✅ 你输入的是：", y)

# 3. raise：手动抛出异常
# 如果条件不符合，可以手动触发异常
x = 10
if x > 5:
    raise Exception(f"x 不能大于 5，当前 x = {x}")

# 4. 自定义异常类（继承 Exception）
# 自定义异常类型
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"自定义异常：{self.value}"

# 使用自定义异常
def check_score(score):
    if score < 0 or score > 100:
        raise MyError(f"成绩不合法：{score}")

try:
    check_score(150)
except MyError as e:
    print(e)

# 5. try/finally：一定会执行的清理代码
# 演示 finally 块无论是否出错都会执行
try:
    print("程序运行中...")
    x = 1 / 0  # 此处故意抛出 ZeroDivisionError
finally:
    print("✅ finally：无论是否异常我都会执行！")