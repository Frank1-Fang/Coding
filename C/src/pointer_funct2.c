#include <stdio.h>

// 四个运算函数
int add(int a, int b) { return a + b; }
int sub(int a, int b) { return a - b; }
int mul(int a, int b) { return a * b; }
int divide(int a, int b) {
    if (b == 0) {
        printf("除数不能为 0！\n");
        return 0;
    }
    return a / b;
}

int main() {
    int a, b, choice;
    int result;

    // 函数指针数组，对应 1-4 菜单选项
    int (*operations[4])(int, int) = { add, sub, mul, divide };

    printf("请输入两个整数: ");
    scanf("%d %d", &a, &b);

    printf("请选择操作:\n");
    printf("1. 加法\n");
    printf("2. 减法\n");
    printf("3. 乘法\n");
    printf("4. 除法\n");
    printf("你的选择（1-4）: ");
    scanf("%d", &choice);

    if (choice >= 1 && choice <= 4) {
        // 使用函数指针数组调用对应函数
        result = operations[choice - 1](a, b);
        printf("结果是: %d\n", result);
    } else {
        printf("无效的选择。\n");
    }

    return 0;
}

// 指针函数的优点: 1. 多个函数中动态选择，2. 把函数作为参数传入另一个函数
