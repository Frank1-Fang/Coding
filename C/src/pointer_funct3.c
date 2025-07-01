#include <stdlib.h>
#include <stdio.h>
// 回调函数：被当做参数传给另一个函数的函数
// getNextRandomValue 是一个回调函数，不接受输入，返回一个 int 类型的输出
// 其他函数通过函数指针（这里是 int (*getNextValue)(void)）来调用这个函数
// getNextValue() 在函数 populate_array 中可以被反复调用
// 注意：populate_array(myarray, 10, getNextRandomValue()); 是错误的！！因为 getNextRandomValue() 意味着函数被立即执行！


void populate_array(int *array, size_t arraySize, int (*getNextValue)(void))
{
    for (size_t i=0; i<arraySize; i++)
        array[i] = getNextValue();
}

// 获取随机值
int getNextRandomValue(void)
{
    return rand();
}

int main(void)
{
    int myarray[10];
    /* getNextRandomValue 不能加括号，否则无法编译，因为加上括号之后相当于传入此参数时传入了 int , 而不是函数指针*/
    populate_array(myarray, 10, getNextRandomValue);
    for(int i = 0; i < 10; i++) {
        printf("%d ", myarray[i]);
    }
    printf("\n");
    return 0;
}
