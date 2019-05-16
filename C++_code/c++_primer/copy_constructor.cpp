#include <iostream>
using namespace std;

class CExample{
public:
    CExample():a(0){}
    CExample(int b){
        a = b;
        printf("constructor is called\n");
    };
    CExample(const CExample &c):a(c.a)
    {
        //a = c.a;
        //printf("copy constructor is called\n");
        cout<<"copy constructor is called"<<endl;
    }
    ~CExample(){
        printf("destuctor is called\n");
    };
    void show(){
        cout << a << endl;
    };
    CExample &operator=(const CExample &)=delete;

    CExample(CExample &&tmp):a(tmp.a)
    {
        
        cout<<"hello lizhi"<<endl;
    }
private:
    int a;
};

// 当函数的参数为类的对象时
// void g_fun(CExample c){
    // cout << "g_fun is called" << endl;
// }
/*
constructor is called

copy constructor is called
100
copy constructor is called
g_fun is called
destuctor is called
destuctor is called
destuctor is called
*/

//这里是对象的引用
// void g_fun(CExample &c){
//     cout << "g_fun is called" << endl;
// }
/*
constructor is called
copy constructor is called
100
g_fun is called
destuctor is called
destuctor is called
*/

//当函数返回值为对象时
CExample g_fun(){
    CExample temp(3);
    cout << "g_fun" << endl;
    return temp;
}
// constructor is called
// destuctor is called


class A{
private:
    int a;
public:
    A():a(0){}
    A(const A&tmp){
        a=tmp.a;
        cout<<"aaaaaaa"<<endl;
    }
    void show(){
        cout << "i am here" << endl;
    }
};

A func()
{
    A tmp;
    return tmp;
}
int main(){
    // CExample A(100);
    // CExample B = A;
    // B.show();
    //CExample test(1);
    //CExample test1(test);
    //CExample e=g_fun();
    //e.show();
    A aaa;
    A bbb = func();
    bbb.show();
    return 0;
}

