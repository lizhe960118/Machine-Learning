/*
#include <iostream>
using namespace std;

class Point{
    int x, y;
public:
    Point(int a, in b){x = a; y = b};
    Void MovePoint(int a, int b){x += a; y +=b};
    Void print(){cout << "x=" << x << "y=" << y << endl};
};

int main(){
    Point cur_point(10, 10);
    cur_point.MovePoint(2, 2); 
    //当在类的非静态成员函数中访问类的非静态成员的时候，编译器会自动将对象本身的地址作为一个隐含参数传递给函数
    //当cur_point调用MovePoint函数时，将cur_point的地址传递给了this指针
    //任何对类成员的直接访问都被看成this的隐式使用。
    cur_point.print();
    return 0;
}
*/

/*
#include <iostream>
using namespace std;

class A{
public:
    int get() const{return i;}
    void set(int x) {this->i = x; cout << "this 指针保存的内存地址为:" << this << endl;} 
private:
    int i;
    //this 指针被隐含地声明为: ClassName *const this，这意味着不能给 this 指针赋值；
};

int main(){
    A a;
    a.set(9);
    cout << "a的指针为" << &a << endl;
    cout << "a保存的值为：" << a.get() << endl;
    A b;
    b.set(99);
    cout << "b的指针为" << &b << endl;
    cout << "b保存的值为" << b.get() << endl;
    return 0;
}
*/

/*
#include <iostream>
using namespace std;

class A{
    int i;
 public:
    void Hello(){
        cout << "hello" << endl;
    }
};

int main(){
    A* p = NULL;
    p->Hello();
    // 依旧可以输出hello，
    // cout语句中没有用到this指针，依旧可以输出结果
}
*/

#include <iostream>
using namespace std;

class Complex{
 public:
    double real, imag;
    Complex(double r, double i):real(r), imag(i){}
    Complex AddOne(){
        this->real++;
        return *this;
    }
};

int main(){
    Complex c1(1, 1), c2(0,0);
    c2 = c1.AddOne();
    cout << c2.real << "," << c2.imag << endl;
    return 0;
}
// 因为静态成员函数并不作用于某个对象，所以在其内部不能使用 this 指针