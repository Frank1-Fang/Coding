#include <stdio.h>

// 递归实现阶乘
int factorial(int n) {
    if (n == 0 || n == 1)
        return 1;  // 终止条件
    else
        return n * factorial(n - 1);  // 递归调用
}

int main() {
    int num = 5;
    printf("%d 的阶乘是 %d\n", num, factorial(num));
    return 0;
}
