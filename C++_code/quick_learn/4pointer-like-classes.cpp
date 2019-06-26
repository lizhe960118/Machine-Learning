#include <iostream>
using namespace std;

// 智能指针
template <class T> 
class my_shared_ptr {
public: 
    T& operator*() const {
        return *px;
    }
    T* operator->() const {
        // return &(operator*());
        return px;
    }
    my_shared_ptr(T* p):px(p){}
private: 
    T* px;
    long* pn;
};

struct Foo{
    void method(){
        cout << "Foo.method" << endl; 
    }
};

int main(){
    my_shared_ptr<Foo> sp(new Foo);
    Foo f(*sp); // sp内部指针指向Foo类型的元素，*sp像指针一样调用
    sp->method(); // 通过指针px调用method();
}