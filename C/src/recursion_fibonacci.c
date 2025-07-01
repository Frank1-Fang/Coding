#include <stdio.h>

// 递归实现斐波那契
int fibonacci(int n) {
    if (n == 0)
        return 0;  // base case 1
    else if (n == 1)
        return 1;  // base case 2
    else
        return fibonacci(n - 1) + fibonacci(n - 2);  // 递归调用
}

int main() {
    int i, terms = 10;
    printf("前 %d 项斐波那契数列为：\n", terms);
    for (i = 0; i < terms; i++) {
        printf("%d ", fibonacci(i));
    }
    printf("\n");
    return 0;
}
