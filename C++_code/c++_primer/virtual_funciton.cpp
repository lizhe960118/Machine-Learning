/*
//example 1
#include<iostream>
using namespace std;

class A{
public:
    virtual void out1() = 0;
    virtual ~A(){};
    virtual void out2(){
        cout << "A(out2)" << endl;
    }
    void out3(){
        cout << "A(out3)" << endl;
    }
};

class B:public A{
public:
    virtual ~B(){};
    void out1(){
        cout << "B(out1)" << endl;
    }
    void out2(){
        cout << "B(out2)" << endl;
    }
    void out3(){
        cout << "B(out3)" << endl;
    }
};

int main(){
    A *ab = new B;
    ab->out1();
    ab->out2();
    ab->out3();
    cout << "*********" << endl;
    B *bb = new B;
    bb->out1();
    bb->out2();
    bb->out3();

    delete ab;
    delete bb;
    return 0;

}
*/

#include <iostream>
using namespace std;
class A{
public:
    virtual void foo(){
        cout << "A::foo() is called" << endl;
    }
};

class B:public A{
public:
    void foo(){
        cout << "B::foo() is called" << endl;
    }
};

int main(){
    A *a = new B;
    a->foo();
    return 0;
}
//定义一个函数为虚函数，不代表函数为不能被实现的函数
//定义一个函数为虚函数是为了允许用基类的指针来调用子类的这个函数

//定义纯虚函数才代表这个函数没有被实现
//定义纯虚函数是为了实现一个接口，起到一个规范的作用，规范继承这个类时程序员必须实现这个函数
