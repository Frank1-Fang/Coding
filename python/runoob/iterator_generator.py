# 1. Iterator
# 迭代器是一个可以记住遍历的位置的对象
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退
# 迭代器有两个基本的方法：iter() 和 next()
# 字符串，列表或元组对象都可用于创建迭代器
list = [1, 2, 3, 4]
it = iter(list)    # 创建迭代器对象
print (next(it))   # 输出迭代器的下一个元素
print (next(it))
print (next(it))
print (next(it))
print ("---")
# 迭代器对象可以使用常规for语句进行遍历
list2 = [1, 2, 3, 4]
it2 = iter(list2)
for x in it2:
    print (x)
print ("---")
# 2. Generator
# 在 Python 中，使用了 yield 的函数被称为生成器（generator）
# yield 是一个关键字，用于定义生成器函数
# 生成器函数是一种特殊的函数，可以在迭代过程中逐步产生值，而不是一次性返回所有结
def countdown(n):
    while n > 0:
        yield n
        n -= 1
 
# 创建生成器对象
generator = countdown(5)
 
# 通过迭代生成器获取值
print(next(generator))  # 输出: 5
print(next(generator))  # 输出: 4
print(next(generator))  # 输出: 3
 
# 使用 for 循环迭代生成器
for value in generator:
    print(value)  # 输出: 2 1
