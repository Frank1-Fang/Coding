// config.c - 可配置预处理器演示程序
#include <stdio.h>   // 标准输入输出
#include <stdlib.h>  // rand()

// 1. 定义一个宏常量
#define MAX_VALUE 100

// 2. 宏函数：返回较大值
#define MAX(x, y) ((x) > (y) ? (x) : (y))

// 3. 条件编译：是否启用调试模式
#define DEBUG_MODE

// 4. 主程序入口
int main() {
    int a = rand() % MAX_VALUE;
    int b = rand() % MAX_VALUE;

    printf("随机数 A = %d, B = %d\n", a, b);
    printf("较大值是：%d\n", MAX(a, b));

#ifdef DEBUG_MODE // 如果 DEBUG_MODE 已经被定义，则输出 [调试模式]...
    printf("[调试模式] A 和 B 已成功生成。\n");
#else
    printf("[发布模式] 运行正常。\n");
#endif

#ifndef VERSION // 如果 VERSION 没有被定义，那么就定义 VERSION 为 "1.0.0"
    #define VERSION "1.0.0"
#endif

    printf("当前程序版本：%s\n", VERSION);

#if MAX_VALUE > 1000 // 利用宏定义 来编写判断语句 if-endif
    #error "MAX_VALUE 太大了！请减小以节省内存。"
#endif

    return 0;
}
