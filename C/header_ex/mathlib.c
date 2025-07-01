#include "global.h"
#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int multiply(int a, int b) {
    return a * b;
}

#ifdef ENABLE_DEBUG
void debug_log(const char* msg) {
    printf("[DEBUG] %s\n", msg);
}
#endif
