// 将一个正整数分解质因数。例如：输入 90,打印出 90=2*3*3*5。
#include <stdio.h>
int main(){
    int number_input = 0;
    scanf("%d", &number_input);
    printf("%d = ", number_input);
    for (int i = 2; i <= number_input; i++){
        while(number_input % i == 0){
            printf("%d", i);
            number_input = number_input / i;
            if (number_input != 1){
                printf("*");
            }
        }
    }
    printf("\n");
    return 0;
}