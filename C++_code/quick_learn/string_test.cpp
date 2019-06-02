#include <iostream>
#include "mystring.h"

using namespace std;

int main(){
    MyString s1; //这里调用默认构造函数
    // cout << *s1.get_c_str() << endl;
    // MyString s1("1");
    MyString s2("hello");

    s1 = "world"; //这里回事？
    MyString s3(s1);
    cout << s3.get_c_str() << endl;
    
    s3 = s2;
    cout << s3.get_c_str() << endl;
    return 0;
}