// 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数 本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

#include <stdio.h>

typedef struct {
    int ones;
    int tens;
    int hundreds;
} Digits;


Digits check_digit(int number) {
    Digits d;
    d.ones = number % 10;
    d.tens = (number / 10) % 10;
    d.hundreds = (number / 100) % 10;
    return d;
}

int check_Amstrong(int x, int y, int z, int number){
    int sum =  x * x * x + y * y * y + z * z * z;
    if (sum == number) {return 1;} else {return 0;}
}

int main() {
    int i;

    // 遍历 100 到 999 的数字
    for (i = 100; i < 1000; i++) {
        Digits result = check_digit(i);

        if (check_Amstrong(result.ones, result.tens, result.hundreds, i) == 1){
            printf("%d\n", i);
        }
    }

    return 0;
}
