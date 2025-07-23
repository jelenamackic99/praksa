#include <stdio.h>
#include <stdint.h>
#include <stdarg.h>
void printBinary (int num){
    for (int i=0; i<32; i++){
        int bit = num & (1<<31)?1:0;
        num=num<<1;
        printf("%d", bit);
    }
}

int32_t htonl(int32_t num){
    int32_t pom=0;
    for(int i=1;i<=4;i++){
        pom=pom | ((num >> (8 * i)) & 0xFF) << (8 * (3 - i));
    }
    return pom;
}


int32_t ntohl(int32_t num){
    int32_t pom=0;
    for(int i=0;i<4;i++){
        pom=pom | ((num >> (8 * i)) & 0xFF) << (8 * (3 - i));
    }
    return pom;
}

int32_t factorial(int32_t num){
    int32_t fact=1;
    if(num>1){   
        fact=factorial(num-1)*num;    
    }
    return fact;
}

int32_t fibonacci(int32_t num){
    int32_t fibb;
    if (num==0) return 0;
    else if(num==1) return 1;
    else return fibonacci(num-1) + fibonacci(num-2);
   
}

double arithemitc(int32_t cnt,...) {
    if (cnt<=0) return 0;
    va_list args; 
    va_start(args,cnt);
    double sum=0;
    for(int i=0;i< cnt ; i++){
        sum += va_arg(args,int); // cita prvi arg poslije cnt(0-tog)
    }
    va_end(args);
    return (sum/cnt);

}

    
