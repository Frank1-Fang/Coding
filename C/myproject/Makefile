# =============================
# 变量定义
# =============================

# 编译器
CC = gcc

# 编译选项
CFLAGS = -Wall -g

# 源文件
SRC_MAIN = main.c
SRC_UTILS = utils.c

# 目标文件
OBJ_MAIN = main.o
OBJ_UTILS = utils.o

# 可执行文件名称
TARGET = myapp

# =============================
# 默认目标：编译整个程序
# =============================

all: $(TARGET)


# =============================
# 生成最终可执行文件
# =============================

$(TARGET): $(OBJ_MAIN) $(OBJ_UTILS)
	@echo "🔧 Linking object files into executable: $(TARGET)"
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJ_MAIN) $(OBJ_UTILS)


# =============================
# 编译 main.c -> main.o
# =============================

$(OBJ_MAIN): $(SRC_MAIN)
	@echo "🛠️  Compiling $(SRC_MAIN) -> $(OBJ_MAIN)"
	$(CC) $(CFLAGS) -c $(SRC_MAIN) -o $(OBJ_MAIN)


# =============================
# 编译 utils.c -> utils.o
# =============================

$(OBJ_UTILS): $(SRC_UTILS)
	@echo "🛠️  Compiling $(SRC_UTILS) -> $(OBJ_UTILS)"
	$(CC) $(CFLAGS) -c $(SRC_UTILS) -o $(OBJ_UTILS)


# =============================
# 清理命令：删除 .o 和最终文件
# =============================

clean:
	@echo "🧹 Cleaning up..."
	rm -f $(OBJ_MAIN) $(OBJ_UTILS) $(TARGET)

# =============================
# 附加目标（伪目标）：避免与实际文件名冲突
# =============================

.PHONY: all clean
