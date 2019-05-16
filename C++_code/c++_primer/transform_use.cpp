/*
// static_cast
#include <iostream>
using namespace std;

class A{
public:
    operator int() {return 1;}
    operator char*() {return NULL;}
}

int main(){
    A a;
    int n;
    char *p = "New Dragon Inn";
    n = static_cast<int>(3.14);
    n = static_cast<int>(a);
    p = static_cast<char *>(a);
    n = static_cast<int>(p); // invalid static_cast from type 'char*' to type 'int'
    p = static_cast<char *>(n); // invalid static_cast from type 'int' to type 'char*'
    return 0;
}
*/

/*
//reinterpert_cast 用于进行各种不同类型的指针之间的转换，转换时执行的事逐比特得到复制
#include<iostream>
using namespace std;

class A{
public:
    int i;
    int j;
    A(int n):i(n),j(n){}
};

int main(){
    A a(100);
    int &r = reinterpret_cast<int &>(a); //强行让r引用a
    r = 200;
    cout << a.i << "," << a.j << endl;
    
    int n = 300;
    A* pa = reinterpret_cast<A*>(&n);//强行让pa指向n
    pa->i = 400;
    pa->j = 500;
    cout << n << endl;

    long long la = 0x12345678abcdLL;
    pa = reinterpret_cast<A*>(&la);
    // cout << *pa << endl;
    unsigned int *u = reinterpret_cast<unsigned int *>(pa);
    cout << hex << *u << endl;

    typedef void (* PF1) (int);
    typedef int (* PF2) (int, char *);
    PF1 pf1; PF2 pf2;
    pf2 = reinterpret_cast<PF2>(pf1);
    system("pause");
    return 0;
}
*/

/*
//const_cast 用于去除const属性的转换
#include<iostream>
using namespace std;

int main(){
    const string s = "Inception";
    string& p = const_cast<string&>(s);
    cout << p << endl;
    string* ps = const_cast<string*>(&s); // &s 的类型是const string *
    cout << *ps << endl;
    system("pause");
    return 0;
}
*/

//dynamic_cast
//专门讲多态基类的指针或引用强制转换为派生类
#include <iostream>
#include <string>
using namespace std;

class Base{
public:
    virtual ~Base(){}
};

class Derived:public Base{

};

int main(){
    Base b;
    Derived d;
    Derived *pd;
    pd = reinterpret_cast <Derived*>(&b); //强制转换为指向基类的指针
    if (pd == NULL){
        cout << "unsafe reinterpret_cast" << endl; //不会执行
    }
    pd = dynamic_cast <Derived*>(&b);
    if (pd == NULL){
        cout << "unsafe dynamic_cast1" << endl;
    }
    pd = dynamic_cast <Derived*>(&d);
    if(pd == NULL){
        cout << "unsafe dynamic_cast2" <<endl;
    }
    system("pause");
    return 0;
}



