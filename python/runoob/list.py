# 访问列表中的值
print("----------------------------访问列表中的值----------------------------")
list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print("当前列表为: ", list)
print("列表中的第一个元素是: ", list[0]) 
print("列表中的第二个元素是: ", list[1])
print("列表中的第三个元素是: ", list[2])


# 从右往左倒序输出
print("列表中从右往左第一个元素是: ", list[-1])  # black
print("列表中从右往左第二个元素是: ", list[-2]) # white
print("列表中从右往左第三个元素是: ", list[-3])  # yellow


nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print("当前列表为: ", nums)
print("列表第1~4个元素是: ", nums[0:4]) # [10, 20, 30, 40]

print("----------------------------更新列表中的值----------------------------")
# 更新列表
# 直接用 list_name[index] 访问列表中的元素，然后对其进行赋值从而修改 
list1 = ['Google', 'Runoob', 1997, 2000]
print("当前列表为: ", list1)
print ("第三个元素为 : ", list1[2])
list1[2] = 2001
print ("更新后的第三个元素为 : ", list1[2])

# 使用 appen() 函数，在列表的最后添加元素
list2 = ['Google', 'Runoob', 'Taobao']
print("当前列表为: ", list2)
list2.append('Baidu')
print ("更新后的列表 : ", list2)

# 使用 del() 函数，删除列表中的元素
list3 = ['Google', 'Runoob', 1997, 2000]
print("当前列表为: ", list3)
del list3[2]
print ("删除第三个元素 : ", list3)
