//类模板：一种做饼干的模子
//模板类：一种饼干，类模板实例化之后的产物

//类模板：允许用户为类定义一种模式，使得类中的某些数据成员、默认成员函数的参数，某些成员函数的返回值
//能够取任意类型

#include <iostream>
using namespace std;

template <class T> //定义模板
class Test{
private:
    T n;
    const T i;
public:
    Test():i(0){}
    Test(T k);
    ~Test();
    void print();
    T operator+(T x);
};

template<class T>
void Test<T>::print(){
    cout << "n=" << n << endl;
    cout << "i=" << i << endl;
}

template<class T>
Test<T>::Test(T k):i(k){
    n = k;
}

template<class T>
T Test<T>::operator+(T x){
    return n + x;
}

int main(){
    return 0;
}