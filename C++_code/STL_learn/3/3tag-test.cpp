#include <iostream>
using namespace std;

struct B {};
struct D1 : public B {};
struct D2 : public D1 {};

template <class I>
void func(I &p, B){
    cout << "B vision" << endl;
}

template <class I>
void func(I &p, D2){
    cout << "D2 vision" << endl;
}

int main(){
    int *p;
    func(p, B());
    func(p, D1()); // 参数与参数未能直接吻合，由继承关系自动传递调用
    func(p, D2());
    return 0;
}