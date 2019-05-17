// operator ->
#include <iostream>
using namespace std;

class A{
public:
    void display(){
        cout << "A::display()" << endl;
    }
};

// 使得P对象表现得像A类型的指针
// 可以直接调用 p->display
class P{ 
public:
    P(A &ra):ptr(&ra){}
    A* operator->() { //重构->：返回指向A类型的指针
        return ptr;
    }
private:
    A *ptr;
};

class PP{
public:
    PP(A &ra):p(ra){}
    P operator->(){ //返回一个p类型的对象， 会递归到返回A类型的指针
        return p;
    } 
private:
    P p;
};

int main(){
    A a;
    P p(a);
    p->display();
    cout << endl;

    PP pp(a);
    pp->display();
    cout << endl;
    system("pause");
    return 0;
}
