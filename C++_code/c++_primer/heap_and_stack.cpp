#include <iostream>
#include <stdlib.h>

int a = 0; //全局初始化区
char *p1; //全局未初始化区

int main(){
    int b; //栈
    char s[]= "abc";
    char *p2;
    char *p3 = "123456"; //123456\0在常量区
    static int i = 0; // 全局初始化区
    char *p4 = (char *)malloc(10); //分配的字节在堆区
    return 0;
}