#include <stdio.h>

int main(int argc, char *argv[]) {
    printf("你输入了 %d 个参数（包含程序本身）：\n", argc);

    for (int i = 0; i < argc; i++) {
        printf("参数 %d: %s\n", i, argv[i]);
    }

    return 0;
}
