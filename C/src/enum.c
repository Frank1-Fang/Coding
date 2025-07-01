#include <stdio.h>
// enum（枚举） 是 C 语言中的一种用户自定义数据类型，用于定义一组命名的整数常量。
// 特别适合表示状态、选项、星期等固定集合的值

enum Weekday {
    MON = 1,
    TUE,
    WED,
    THU,
    FRI,
    SAT,
    SUN
};

int main() {
    enum Weekday today;

    today = WED;

    if (today == WED) {
        printf("今天是星期三！\n");
    }

    printf("today 的数值是：%d\n", today);  // 输出 3
    return 0;
}
