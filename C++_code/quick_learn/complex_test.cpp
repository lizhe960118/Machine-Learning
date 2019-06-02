#include <iostream>
#include "complex.h" //自定义的使用双引号

using namespace std;

int main(){
    complex c1(2, 1);
    complex c2;
    cout << c1;
    cout << c2; // (0,0)

    c2 = c1 + 5;
    cout << c2; // (7,1)
    c2 = 7 + c1;
    cout << c2; // (9,1)
    c2 = c1 + c2;
    cout << c2; // (11, 2)
    c2 += c1;
    cout << c2; // (13, 3)
    c2 += 3; // ? 可以直接加double c2 = c2 + 3
    cout << c2; // (16, 3)
    c2 = -c1;
    cout << c2; // (-2, -1)

    cout << (c1 == c2) << endl;
    cout << (c1 != c2) << endl;
    // cout << conj(c1) << endl;

    return 0;
}