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

template <class T, class Sequence> 
class stack_test;
template <class T, class Sequence> 
bool operator== (const stack_test<T, Sequence>&x,
                const stack_test<T, Sequence>&y);
template <class T, class Sequence> 
bool operator< (const stack_test<T, Sequence>&x,
                const stack_test<T, Sequence>&y);

// 根据前一个参数T，设定下一个参数Sequence的默认值为 deque_test<T>
template <class T, class Sequence = deque_test<T> > 
class stack_test{
    friend bool operator== <T> (const stack_test<T>&, const stack_test<T>&);
    friend bool operator< <T> (const stack_test<T>&, const stack_test<T>&);

    friend bool operator== <T> (const stack_test&, const stack_test&);
    friend bool operator< <T> (const stack_test&, const stack_test&);
    
    friend bool operator== <> (const stack_test&, const stack_test&);
    friend bool operator< <> (const stack_test&, const stack_test&);
    
public: 
    stack_test(){
        cout << "stack_test" << endl;
    }
private: 
    Sequence c;
};

template <class T, class Sequence> 
bool operator== (const stack_test<T, Sequence>& x, 
                const stack_test<T, Sequence>& y){
    cout << "operator == " << '\t';
    return true;
}

template <class T, class Sequence> 
bool operator< (const stack_test<T, Sequence>& x, 
                const stack_test<T, Sequence>& y){
    cout << "operator < " << '\t';
    return true;
}

int main(){
    stack_test<int> x;
    stack_test<int> y;
    
    cout << (x == y) << endl;
    cout << (x < y) << endl;

    // stack_test<char> y2;
    // cout << (x == y2) << endl;
    // cout << (x < y2) << endl;

    return 0;
}

