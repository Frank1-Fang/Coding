// 题目：输入三个整数 x、y、z，请把这三个数由小到大输出。
#include <stdio.h>
void swap(int *a, int *b);

int main(){
    int x, y ,z;
    printf("\n请输入三个整数x, y, z:\n");
    scanf("%d %d %d", &x, &y, &z);
    if (x > y){
        swap(&x, &y);
    }
    if (x > z){
        swap(&x, &z);
    }
    if (y > z){
        swap(&y, &z);
    }
    printf("由小到大排序为: %d, %d, %d\n", x, y, z);
}

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}
