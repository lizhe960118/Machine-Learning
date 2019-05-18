#include<iostream>
#include<cstddef>
using namespace std; 

class alloc_test{
};

template <class T, class Alloc = alloc_test, size_t BufSiz=0> 
class deque_test{
public:
    deque_test(){
        cout << "duque_test" << endl;
    }
};

// 根据前一个参数T，设定下一个参数Sequence的默认值为 deque_test<T>
template <class T, class Sequence = deque_test<T> > 
class stack_test{
public: 
    stack_test(){
        cout << "stack_test" << endl;
    }
private: 
    Sequence c;
};

int main(){
    stack_test<int> x;
    return 0;
}