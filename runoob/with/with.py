# ===============================================
# Python 文件操作笔记：with 关键字与文件打开模式 
# ===============================================

# ✅ 一、with 语句简介：
# with 是 Python 提供的上下文管理协议，用于简洁、安全地管理资源（如文件、数据库连接）。
# 语法形式：
# with open(filename, mode) as file:
#     操作文件
# 使用 with 可自动调用 file.__enter__() 和 file.__exit__()，即使发生异常也能安全关闭资源。

# ✅ 二、文件打开模式（file mode）详解：

# 模式   含义                        文件不存在时     是否清空内容     是否可读     是否可写
# -----  ---------------------------  --------------  --------------  ----------  ----------
# 'r'    只读模式                      ❌ 报错           ❌               ✅          ❌
# 'w'    写入模式（清空或创建）        ✅ 创建           ✅               ❌          ✅
# 'a'    追加写入（写在文件尾）        ✅ 创建           ❌               ❌          ✅
# 'x'    独占创建写入（存在报错）      ✅ 创建           ❌               ❌          ✅
# 'r+'   读写（不清空）                ❌ 报错           ❌               ✅          ✅
# 'w+'   写读（先清空）                ✅ 创建           ✅               ✅          ✅
# 'a+'   追加读写                      ✅ 创建           ❌               ✅          ✅

# ✅ 三、二进制模式（加 'b'）：
# - 'rb' : 以二进制只读（如读取图片）
# - 'wb' : 以二进制写入
# - 'ab' : 以二进制追加
# - 可与 '+' 连用：如 'rb+', 'wb+'

# ✅ 四、示例：只读文件内容
# with open("input.txt", "r") as f:
#     content = f.read()
#     print(content)

# ✅ 示例：写入文件（清空原内容）
# with open("output.txt", "w") as f:
#     f.write("Hello, Debian!")

# ✅ 示例：追加内容到日志文件
# with open("log.txt", "a") as log:
#     log.write("程序执行结束\n")

# ✅ 示例：同时读写
# with open("data.txt", "r+") as f:
#     original = f.read()
#     f.seek(0)
#     f.write("覆盖开头")

# ✅ 示例：读写二进制（如图像）
# with open("image.png", "rb") as img:
#     data = img.read()

# ✅ 示例：处理多个文件
# with open("input.txt", "r") as fin, open("output.txt", "w") as fout:
#     for line in fin:
#         fout.write(line.upper())

# ✅ 五、小结记忆：
# - 读 → r；写 → w；追加 → a；创建 → x
# - 可读写 → 加 + 号，如 r+、w+
# - 二进制 → 加 b，如 rb、wb+
# - 使用 with 可以自动关闭文件，是推荐的文件操作方式

# ✅ 六、常见异常处理（FileNotFoundError 等）
# try:
#     with open("nofile.txt", "r") as f:
#         data = f.read()
# except FileNotFoundError:
#     print("文件未找到！")
# except Exception as e:
#     print("发生其他错误：", e)

try:
    with open("input.txt", "r") as fin, open("output.txt", "w") as fout:
        for line in fin:
            fout.write(line.upper())
    print("文件处理完成：已将内容转为大写写入 output.txt")
except FileNotFoundError:
    print("文件 input.txt 不存在！")
except Exception as e:
    print("发生错误：", e)