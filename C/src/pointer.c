#include <stdio.h>

int main(){
    int var_example = 10;
    int *p = &var_example; // 用 int *来声明变量 p 为指针变量，变量 p 存储的即为变量 var_example 的地址
                           // 我们采用 *p 的方式来访问 p 所存的地址指向的变量，这里即为 var_example = 10
    printf("var_example变量的地址是：%p\n", p);
    printf("*p 代表的就是 var_example 表示的值：%d\n", *p);
    return 0;
}

// *p = v: 把 v 的值 写入 p 指向的内存地址，修改地址中的内容
// p = v: 把 v（应为地址）赋值给指针 p 本身，修改指针本身的值
