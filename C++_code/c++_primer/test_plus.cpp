#include <iostream>
#include <stdlib.h>

using namespace std;

int main(){
    int i = 1;
    printf("%d, %d\n", ++i, ++i);
    printf("%d, %d\n", ++i, i++);
    return 0;
}