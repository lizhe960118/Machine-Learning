#include <iostream>
using namespace std;

class INT_test{
    friend ostream& operator<<(ostream& os, const INT_test&i);
public:
    INT_test(int i):m_i(i){};
    INT_test& operator++(){
        ++(this->m_i);
        return *this;
    }
    const INT_test operator++(int){
        INT_test temp = *this;
        ++(*this);
        return temp;
    }

    INT_test& operator--(){
        --(this->m_i);
        return *this;
    }

    const INT_test operator--(int){
        INT_test temp = *this;
        --(*this);
        return temp;
    }

    int& operator*() const{
        return (int&)m_i; // 确实要将 const int 转为 non-const lvalue
    }
    
private:
    int m_i;
};

ostream& operator<<(ostream& os, const INT_test& i){
    os << '[' << i.m_i << ']';
    return os;
}

int main(){
    INT_test I(5);
    cout << I++; // [5]
    cout << ++I; // [7]
    cout << I--; // [7]
    cout << --I; // [5]
    cout << *I; // 5
    return 0;
}