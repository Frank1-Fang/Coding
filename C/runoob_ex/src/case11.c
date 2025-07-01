// 题目：古典问题（兔子生崽）：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？（输出前40个月即可）
#include <stdio.h>

int main(){

    long long f1 = 1, f2 = 1, fn = 0;
    printf("前40个月的兔子总数如下：\n");

    printf("第1个月: %lld 对\n", f1);
    printf("第2个月: %lld 对\n", f2);

    for (int k =3; k <= 40; k++){
        fn = f1 + f2;
        printf("第%d个月: %lld 对\n", k, fn);
        f1 = f2;
        f2 = fn;
    }
    return 0;
}
