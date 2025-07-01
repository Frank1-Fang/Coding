# 原始字符串
s = "   hello World 123   "
print("原始字符串：", repr(s))  # repr(): 返回一个 对象的官方字符串表示（representation）
                                # 常用于调试、打印字符串带有特殊字符的真实样子，例如 \n, 空格等
                                # --------------------------------------------------------------
                                # s = "  hello\nworld  "
                                # print("str():", str(s))    直接打印，换行被解释
                                # print("repr():", repr(s))  打印字符串真实结构
                                # --------------------------------------------------------------
                                # 输出结果：
                                # str():   hello
                                # world  
                                # repr(): '  hello\nworld  '
                                # --------------------------------------------------------------
                                # 在 Python 中，print() 函数 自动调用对象的 str() 方法 来显示结果
                                # 所以我们一般不需要自己手动写 str()
                                # 只需要如 print("2. lower():", s2) 即可，不需要写 str(s2)

# 1. strip() 去除首尾空白
s1 = s.strip()
print("1. strip():", repr(s1))  # 'hello World 123'

# 2. lower() 转为小写
s2 = s1.lower()
print("2. lower():", s2)        # 'hello world 123'

# 3. upper() 转为大写
s3 = s1.upper()
print("3. upper():", s3)        # 'HELLO WORLD 123'

# 4. capitalize() 首字母大写
s4 = s1.capitalize()
print("4. capitalize():", s4)   # 'Hello world 123'

# 5. title() 每个单词首字母大写
s5 = s1.title()
print("5. title():", s5)        # 'Hello World 123'

# 6. swapcase() 大小写互换
s6 = s1.swapcase()
print("6. swapcase():", s6)     # 'HELLO wORLD 123'

# 7. find() 查找子串
index_hello = s1.find("hello")
print("7. find('hello'):", index_hello)  # 0

# 8. startswith() 是否以某子串开头
starts = s1.startswith("hello")
print("8. startswith('hello'):", starts)  # True

# 9. endswith() 是否以某子串结尾
ends = s1.endswith("123")
print("9. endswith('123'):", ends)        # True

# 10. split() 拆分为列表
words = s1.split()
print("10. split():", words)   # ['hello', 'World', '123']

# 11. join() 用 - 连接字符串列表
joined = "-".join(words)
print("11. join():", joined)   # 'hello-World-123'

# 12. isdigit() 判断是否为数字
only_digits = "12345".isdigit()
print("12. isdigit():", only_digits)  # True

# 13. isalpha() 判断是否全为字母
only_alpha = "abcDEF".isalpha()
print("13. isalpha():", only_alpha)   # True

# 14. isalnum() 是否全为字母+数字
alpha_num = "abc123".isalnum()
print("14. isalnum():", alpha_num)    # True

# 15. zfill() 字符串补0（长度至少为8）
zfilled = "42".zfill(8)
print("15. zfill(8):", zfilled)       # '00000042'
