#include <iostream>
using namespace std;

template <class T>
struct plus_test{
    T operator()(const T& x, const T& y) const{
        return x + y;
    }
};

template <class T>
struct minus_test{
    T operator()(const T&x, const T& y) const{
        return x - y;
    }
};

int main(){
    plus_test<int> plusobj;
    minus_test<int> minusobj;

    cout << plusobj(3, 5) << endl;
    cout << minusobj(3, 5) << endl;

    cout << plus_test<int>()(43, 50) << endl;
    cout << minus_test<int>()(43, 50) << endl;

    return 0;
}