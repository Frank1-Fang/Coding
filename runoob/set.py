print("Set（集合）综合示例")

# 创建集合
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("原始集合 a：", a)
print("原始集合 b：", b)

# add()
a.add(10)
print("add(10) 添加元素 10：", a)

# discard()
a.discard(4)
print("discard(4) 删除元素 4（不存在也不报错）：", a)

# remove()
a.remove(3)
print("remove(3) 删除元素 3（不存在会报错）：", a)

# pop()
popped = a.pop()
print("pop() 随机移除一个元素，得到：", popped)
print("移除后的集合：", a)

# clear()
temp = a.copy()
temp.clear()
print("clear() 清空集合后：", temp)

# copy()
copy_a = a.copy()
print("copy() 复制集合副本：", copy_a)

# update()
a.update([20, 21])
print("update([20, 21]) 批量添加元素：", a)

# union()
print("union(b) 求并集（不改变 a）：", a.union(b))

# intersection()
print("intersection(b) 求交集（不改变 a）：", a.intersection(b))

# intersection_update()
a.intersection_update(b)
print("intersection_update(b) 原地求交集后 a：", a)

# difference()
diff = b.difference(a)
print("b.difference(a) 求差集（b 有 a 没有的）：", diff)

# difference_update()
b.difference_update(a)
print("difference_update(a) 删除 b 中与 a 重合的元素：", b)

# symmetric_difference()
s1 = {1, 2, 3}
s2 = {3, 4, 5}
sym = s1.symmetric_difference(s2)
print("symmetric_difference(s2) 得到对称差集（不重复元素）：", sym)

# symmetric_difference_update()
s1.symmetric_difference_update(s2)
print("symmetric_difference_update(s2) 原地对称差集更新：", s1)

# isdisjoint()
print("isdisjoint({9,10}) 判断是否无交集：", a.isdisjoint({9, 10}))

# issubset()
print("{1,2} 是否是 {1,2,3} 的子集：", {1, 2}.issubset({1, 2, 3}))

# issuperset()
print("{1,2,3} 是否是 {1} 的超集：", {1, 2, 3}.issuperset({1}))

# len()
print("len() 返回集合元素个数：", len(a))
