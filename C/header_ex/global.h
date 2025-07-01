#ifndef GLOBAL_H
#define GLOBAL_H

// 全局常量和函数声明
#define VERSION "1.0.0"

int add(int a, int b);      // 声明 add 函数
int multiply(int a, int b); // 声明 multiply 函数

// 有条件引用某部分代码
#ifdef ENABLE_DEBUG
void debug_log(const char* msg);
#endif

#endif
