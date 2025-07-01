#include <stdio.h>

int main() {
    int scores[5] = {75, 88, 92, 64, 81};
    int max = scores[0];

    for (int i = 1; i < 5; i++) {
        if (scores[i] > max) {
            max = scores[i];
        }
    }

    printf("最高分是：%d\n", max);

    return 0;
}
