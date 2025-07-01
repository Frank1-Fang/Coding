#include <stdio.h>

int main() {
    int i = -42;
    unsigned int u = 42;
    float f = 3.1415926;
    double d = 123456.789;
    char c = 'A';
    char str[] = "Hello, world!";
    void* p = &i;

    printf("========== 整型 ==========\n");
    printf("有符号十进制 (%%d): %d\n", i);
    printf("无符号十进制 (%%u): %u\n", u);
    printf("十六进制小写 (%%x): %x\n", u);
    printf("十六进制大写 (%%X): %X\n", u);
    printf("八进制 (%%o): %o\n", u);

    printf("\n========== 浮点数 ==========\n");
    printf("普通浮点数 (%%f): %f\n", f);
    printf("科学计数法小写 (%%e): %e\n", d);
    printf("科学计数法大写 (%%E): %E\n", d);
    printf("自动选择 %%f/%%e (%%g): %g\n", d);
    printf("自动选择 %%f/%%E (%%G): %G\n", d);

    printf("\n========== 字符 & 字符串 ==========\n");
    printf("字符 (%%c): %c\n", c);
    printf("字符串 (%%s): %s\n", str);

    printf("\n========== 指针 ==========\n");
    printf("指针地址 (%%p): %p\n", p);

    printf("\n========== 百分号本体 ==========\n");
    printf("百分号 (%%%%): %%\n");

    printf("\n========== 宽度与精度控制 ==========\n");
    printf("宽度10，保留2位小数 (%%10.2f): %10.2f\n", f);
    printf("左对齐宽度10，保留2位 (%%-10.2f): %-10.2fEND\n", f);
    printf("宽度10，补零 (%%010.2f): %010.2f\n", f);

    return 0;
}
