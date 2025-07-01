#include <stdio.h>
#include <stdlib.h>  // 包含 malloc, calloc, realloc, free

int main() {
    int *arr;
    int i, n;

    printf("请输入数组的大小: ");
    scanf("%d", &n);

    // 1. 使用 calloc 分配内存并初始化为 0
    arr = (int *)calloc(n, sizeof(int));

    if (arr == NULL) {
        printf("内存分配失败！\n");
        return 1;
    }

    // 2. 给数组赋值
    for (i = 0; i < n; i++) {
        arr[i] = i * 2;
    }

    // 3. 打印数组内容
    printf("数组内容：");
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    // 4. 扩容数组
    int new_size = n + 3;
    arr = (int *)realloc(arr, new_size * sizeof(int));
    if (arr == NULL) {
        printf("\n扩容失败！\n");
        return 1;
    }

    // 5. 赋值新元素
    for (i = n; i < new_size; i++) {
        arr[i] = i * 10;
    }

    // 6. 打印扩容后的数组
    printf("\n扩容后数组内容：");
    for (i = 0; i < new_size; i++) {
        printf("%d ", arr[i]);
    }

    // 7. 释放内存
    free(arr);

    printf("\n内存已释放。\n");
    return 0;
}
