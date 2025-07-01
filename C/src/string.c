#include <stdio.h>
#include <string.h>  // 必须包含这个头文件！

int main() {
    char str1[100] = "Hello";  // 注意必须分配足够空间
    char str2[] = "World"; // 自动分配足够的空间
    char str3[100];
    char *pos;

    // 1. strcpy: 复制 str1 到 str3
    strcpy(str3, str1);
    printf("1. strcpy: 复制 str1 到 str3\n");
    printf("1. strcpy: str3 = %s\n", str3);

    // 2. strcat: 拼接 str2 到 str1 后面
    strcat(str1, str2);
    printf("2. strcat: 拼接 str2 到 str1 后面\n");
    printf("2. strcat: str1 = %s\n", str1);  // HelloWorld

    // 3. strlen: 字符串长度
    printf("3. strlen: 字符串长度\n");
    printf("3. strlen: str1 的长度是 %lu\n", strlen(str1));

    // 4. strcmp: 比较字符串
    printf("4. strcmp: 比较字符串\n");
    int cmp = strcmp(str1, str2);
    if (cmp == 0)
        printf("4. strcmp: str1 与 str2 相同\n");
    else if (cmp < 0)
        printf("4. strcmp: str1 小于 str2\n");
    else
        printf("4. strcmp: str1 大于 str2\n");

    // 5. strchr: 查找字符 'o' 在 str1 中第一次出现的位置
    printf("5. strchr: 查找字符 'o' 在 str1 中第一次出现的位置\n");
    pos = strchr(str1, 'o'); // 返回一个指针
    if (pos)
        printf("5. strchr: 'o' 在 str1 中的位置是：%ld\n", pos - str1);
    else
        printf("5. strchr: str1 中没有找到 'o'\n");

    // 6. strstr: 查找字符串 "World" 在 str1 中的位置
    printf("6. strstr: 查找字符串 \"World\" 在 str1 中的位置\n");
    pos = strstr(str1, "World"); // 返回一个指针
    if (pos)
        printf("6. strstr: \"World\" 在 str1 中的位置是：%ld\n", pos - str1);
    else
        printf("6. strstr: str1 中没有找到 \"World\"\n");

    return 0;
}
