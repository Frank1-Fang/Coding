# 1. List Comprehension
# [out_exp_res for out_exp in input_list]
# or [out_exp_res for out_exp in input_list if condition]
# out_exp_res：列表生成元素表达式，可以是有返回值的函数
# for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中
# if condition：条件语句，可以过滤列表中不符合条件的值

names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
print("初始列表为: ", names)
new_names = [name.upper() for name in names if len(name)>3]
print("过滤掉长度小于等于三的名字: ", new_names)

print("计算 30 以内可以被 3 整除的整数")
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

# 2. Dictionary Comprehension
# { key_expr: value_expr for value in collection }
# or { key_expr: value_expr for value in collection if condition 

listdemo = ['Google','Runoob', 'Taobao']
print("初始键列表: ", listdemo)
newdict = {key: len(key) for key in listdemo}
print("将列表中各字符串值为键，各字符串的长度为值，组成键值对: ", newdict)

# 3. Set Comprehension
# { expression for item in Sequence }
# or { expression for item in Sequence if conditional }

print("计算数字 1,2,3 的平方数")
setnew = {i**2 for i in (1,2,3)}
print("集合为: ", setnew)

print("判断字符串中不是 a, b, c 的字符，并将其构造为集合")
a = {x for x in 'abracadabra' if x not in 'abc'}
print("不是 a, b, c 字符组成的集合为: ", a)

# 4. Tuple Comprehension
# (expression for item in Sequence )
# or (expression for item in Sequence if conditional )

print("生成一个由数字1~9构成的元组")
b = (x for x in range(1,10))
print("这个元组是: ", tuple(b))