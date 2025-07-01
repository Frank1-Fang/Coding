#include <stdio.h>

int main() {
    int i;

    printf("=== 使用 for 循环 ===\n");
    for (i = 1; i <= 5; i++) {
        printf("for: %d\n", i);
    }

    printf("\n=== 使用 while 循环 ===\n");
    i = 1;  // 重新初始化 i
    while (i <= 5) {
        printf("while: %d\n", i);
        i++;
    }

    printf("\n=== 使用 do-while 循环 ===\n");
    i = 1;  // 再次初始化 i
    do {
        printf("do-while: %d\n", i);
        i++;
    } while (i <= 5);
    // do-while 的特点：不管是否满足条件，循环至少运行一次

    return 0;
}
