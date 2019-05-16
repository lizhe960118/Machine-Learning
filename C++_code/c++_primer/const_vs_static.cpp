/*
class Test{
public:
    Test():a(0){}
    enum{size1=100, size2=200};
private:
    const int a; //只能在构造函数初始化列表中初始化
    static int b;//只能在类的实现文件中定义并初始化
    const static int c;
}

int Test::b = 0; // static 成员变量不能在构造函数初始化列表中初始化，因为它不属于某个对象
// 静态都将存储在全局变量区域
const int Test::c = 0; //给静态成员变量赋值时，不需要加static修饰符，但要常量要加const

//成员变量：
//区别：static静态成员变量不能在类的内部初始化，在类的内部只是声明，定义必须在类的定义体外部
//const成员变量也不能在类的内部初始化，只能通过构造函数列表初始化，所以对于某个对象是常量，对于类来书是可变的

//成员函数：
// const成员函数不能修改成员变量的值
//static成员函数作为类作用域的全局函数，不能访问类的非静态数据成员。类的静态成员函数没有this指针

*/

//完整的例子
// #ifdef A_H_
// #define A_H_
#include <iostream>
using namespace std;

class A{
public:
    A(int a);
    static void print(); //声明静态函数
private:
    static int aa;// 声明静态成员变量
    static const int count; // 声明常量静态数据成员
    const int bb;//常量数据成员
};

int A::aa = 0; //静态成员的定义 + 初始化
const int A::count = 25; //静态常量成员
A::A(int a):bb(a)// 常量成员初始化
{
    aa += 1; 
}

void A::print(){
    cout << "count=" << count << endl;
    cout << "aa =" << aa <<endl;
}
// #endif

int main(){
    A a(10);
    A::print(); //通过类访问静态成员函数
    a.print(); //通过对象访问静态成员函数
    return 0;
}