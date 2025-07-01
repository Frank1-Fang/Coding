// 题目：判断 101 到 200 之间的素数。
#include <stdio.h>
#include <stdbool.h>

// 函数：判断一个数是否为素数
bool isPrime(int num) {
    // 一些特殊情况
    if (num <= 1) return false;
    if (num <= 3) return true;

    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) return false;
    }

    return true;
}

int main() {
    printf("素数在 101 到 200 之间的列表：\n");

    for (int i = 101; i <= 200; i++) {
        if (isPrime(i)) {
            printf("%d ", i);
        }
    }

    printf("\n");
    return 0;
}
