#include <iostream>
#include <string>

using namespace std;

/*
class Base{
public:
    inline virtual void who(){
        cout << "i am Base::who()" << endl;
    }
    virtual ~Base (){}
};

class Derived:public Base{
public:
    inline void who(){
        cout << "i am Derived::who()" << endl;
    }
};

int main(){
    Base b;
    b.who(); //此处是通过对象来调用的，在编译期间可以确定，所以是可以内联的

    Base *ptr = new Derived();
    ptr->who(); // 此处虚函数通过指针调用，呈现多态性，需要运行期间才能确定，所以不可以内联

    delete ptr;
    ptr = nullptr;

    system("pause");
    return 0;
}
*/


class Base{
public:
    virtual ~Base(){
        cout << "~Base()" << endl;
    }
};

class Derived1:public Base{
public: 
    Derived1():name_(new string("NULL")){}
    Derived1(const string &n):name_(new string(n)){}

    ~Derived1(){
        delete name_;
        cout << "~Derived1():name_ has been deleted" << endl;
    }
private: 
    string *name_;
};

class Derived2:public Base{
public: 
    Derived2():name_(new string("NULL")){}
    Derived2(const string &n):name_(new string(n)){}

    ~Derived2(){
        delete name_;
        cout << "~Derived2():name_ has been deleted" << endl;
    }
private: 
    string *name_;
};

// 静态绑定
/*
int main(){
    Derived1 *d1 = new Derived1();
    Derived2 d2 = Derived2("Bob");
    delete d1;
    return 0;
}
*/

// 动态绑定
int main(){
    Base *b[2] = {
        new Derived1(),
        new Derived2("Bob")
    };
    //指针的静态类型为基类指针，
    //因此在delete时候只会调用基类的析构函数，而不会调用派生类的析构函数。
    for (int i = 0; i < 2; i++){
        delete b[i];
    }
    return 0;
}
