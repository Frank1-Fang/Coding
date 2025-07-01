#include <stdio.h>
#include "global.h"  // 自定义头文件

int main() {
    int x = 5, y = 7;
    printf("加法结果：%d\n", add(x, y));
    printf("乘法结果：%d\n", multiply(x, y));

#ifdef ENABLE_DEBUG
    debug_log("主函数执行完毕！");
#endif

    return 0;
}
// 编译：如果你想启用 debug 功能，使用带宏定义的编译命令：
// gcc -DENABLE_DEBUG main.c mathlib.c -o myapp
// output: 加法结果：12
//         乘法结果：35
//         [DEBUG] 主函数执行完毕！



// 不启用时直接：gcc main.c mathlib.c -o myapp
// output: 加法结果：12
//         乘法结果：35
