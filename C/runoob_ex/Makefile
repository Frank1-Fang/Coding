# 编译器设置
CC := gcc
CFLAGS := -Wall -g

# 目录设置
SRC_DIR := src
BIN_DIR := bin

# ========== 默认：无操作 ==========
all:

# ========== 编译规则：make case1 ==========
.PHONY: $(basename $(notdir $(wildcard $(SRC_DIR)/*.c)))
$(basename $(notdir $(wildcard $(SRC_DIR)/*.c))):
	@mkdir -p $(BIN_DIR)
	$(CC) $(CFLAGS) $(SRC_DIR)/$@.c -o $(BIN_DIR)/$@

# ========== 运行规则：make run case1 ==========
.PHONY: run
run:
	@mkdir -p $(BIN_DIR)
	$(MAKE) $(word 2, $(MAKECMDGOALS))
	./$(BIN_DIR)/$(word 2, $(MAKECMDGOALS))

# ========== 清理规则 ==========
#.PHONY: clean
#clean:
#	rm -f $(BIN_DIR)/*
