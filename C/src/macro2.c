#include <stdio.h>

// 参数化宏：最大值
#define MAX(a, b) ((a) > (b) ? (a) : (b))

// 字符串化：将参数转换为字符串
#define STR(x) #x

// 标识符拼接：生成变量名
#define MAKE_VAR(name, num) name##num

int main() {
    int score1 = 88;
    int score2 = 95;

    printf("最大值是：%d\n", MAX(score1, score2));

    // 预定义宏演示
    printf("当前文件：%s\n", __FILE__);
    printf("当前行号：%d\n", __LINE__);
    printf("编译时间：%s %s\n", __DATE__, __TIME__);
    printf("当前函数：%s\n", __func__);

    // 字符串化演示
    printf("将宏参数变成字符串：%s\n", STR(Hello_World!));

    // 拼接变量名
    int MAKE_VAR(myvar, 3) = 123;  // 相当于 int myvar3 = 123;
    printf("变量拼接结果 myvar3 = %d\n", myvar3);

    return 0;
}
