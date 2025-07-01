print("Pyhton Dictionary 字典综合示例")

# 创建字典
info = {"name": "Alice", "age": 25, "gender": "female"}
print("原始字典：", info)

# len()
print("元素个数：", len(info))

# str()
print("字符串表示：", str(info))

# type()
print("类型：", type(info))

# get()
print("获取 age: ", info.get("age"))
print("获取 address(默认): ", info.get("address", "未知"))

# in
print("是否包含 'name': ", "name" in info)

# setdefault()
info.setdefault("email", "alice@example.com")
print("添加 email: ", info)

# update()
# 将提供的 新字典中的 key-value 加入到原字典中
# 如果 key 已存在，则更新对应的值（覆盖）
# 如果 key 不存在，则新增该键值对
info.update({"age": 30, "city": "Shanghai"})
print("更新后：", info)

# keys(), values(), items()
print("所有键：", list(info.keys()))
print("所有值：", list(info.values()))
print("所有键值对：", list(info.items()))

# pop()
removed = info.pop("gender")
print("删除 gender, 得到: ", removed)

# popitem()
last = info.popitem()
print("popitem() 删除最后项：", last)

# copy()
copy_info = info.copy()
print("复制新字典：", copy_info)

# clear()
info.clear()
print("清空后：", info)

# fromkeys()
new_dict = dict.fromkeys(["a", "b", "c"], 0) # 以 a, b, c 为键，新建一个名为 new_dict 的字典
print("fromkeys() 新字典：", new_dict)
