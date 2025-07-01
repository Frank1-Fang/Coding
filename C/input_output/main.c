#include <stdio.h>
#include <string.h>

int main() {
    char name[50];
    char message[200];
    FILE *fp;

    // 1. 获取用户姓名
    // 利用 fgets 读取命令行中输入的字符串
    printf("请输入你的名字：");
    fgets(name, sizeof(name), stdin); // 使用 fgets 防止溢出

    // 去除换行符
    name[strcspn(name, "\n")] = '\0';

    // 2. 获取留言内容
    printf("请输入你的留言内容：");
    fgets(message, sizeof(message), stdin);

    // 3. 写入文件
    // 利用 fopen 的追加模式 “a" 打开文件 messages.txt
    fp = fopen("messages.txt", "a");  // 追加模式
    if (fp == NULL) {
        printf("文件打开失败！\n");
        return 1;
    }

    // fprintf 是格式化写入函数，将用户名字和留言写入到 messages.txt 中
    fprintf(fp, "用户：%s\n留言：%s\n---\n", name, message);
    fclose(fp);
    printf("留言已保存到文件。\n");

    // 4. 从文件读取全部留言内容并输出
    printf("\n==== 所有留言内容 ====\n");
    fp = fopen("messages.txt", "r");
    if (fp == NULL) {
        printf("无法读取留言文件。\n");
        return 1;
    }

    char line[256];
    while (fgets(line, sizeof(line), fp)) {
        fputs(line, stdout);  // 输出每一行
    }
    fclose(fp);

    // 5. getchar 和 putchar 演示
    char ch;
    printf("\n按任意键退出：");
    ch = getchar();   // 获取字符（可能是之前的换行）
    ch = getchar();   // 再次获取真正按下的字符
    printf("你按下了：");
    putchar(ch);
    printf("\n");

    return 0;
}
