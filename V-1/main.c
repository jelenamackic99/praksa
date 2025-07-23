#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdarg.h>
#include "andjela_curguz.h"
int32_t addNum(int32_t a, int32_t b){
    int32_t res;
__asm__ (
    "movl %1, %%eax\n\t"
    "addl %2, %%eax\n\t"
    "movl %%eax, %0\n\t"
    : "=r"(res)
    : "r"(a),"r"(b)
    :"%eax"
);
    return res;
}


int main() {
    int32_t a=4;
    int32_t b=5;
    double x= arithemitc(3,2,4,5);
    printf("%f", x);
}

