#include <stdio.h>
#include <stdlib.h>

#define INITIAL_SIZE 10

int main() {
    char *buffer;
    int size = INITIAL_SIZE;
    int length = 0;
    int ch;

    // 分配初始内存
    buffer = (char *)malloc(size * sizeof(char));
    if (buffer == NULL) {
        printf("内存分配失败！\n");
        return 1;
    }

    printf("请输入一段文字（回车结束）：\n");

    while ((ch = getchar()) != '\n' && ch != EOF) {
        // 如果缓冲区满了，扩容
        if (length >= size - 1) { // 留一个位置放 \0
            size *= 2;
            char *new_buffer = realloc(buffer, size * sizeof(char));
            if (new_buffer == NULL) {
                printf("内存扩展失败！\n");
                free(buffer);
                return 1;
            }
            buffer = new_buffer;
        }
        buffer[length++] = (char)ch;
    }

    buffer[length] = '\0'; // 添加字符串结束符

    printf("你输入的内容是：%s\n", buffer);

    // 释放内存
    free(buffer);
    return 0;
}
