#include <iostream>
using namespace std;

#define __STL_TEMPLATE_NULL template <>

template <class Key> struct hash_test{
    void operator() (){
        cout << "hash <T>" << endl;
    }
};

__STL_TEMPLATE_NULL struct hash_test<char>{
    void operator()() {
        cout << "hash <char>" << endl;
    }
};

__STL_TEMPLATE_NULL struct hash_test<unsigned char>{
    void operator()() {
        cout << "hash <unsigned char>" << endl;
    }
};

int main(){
    hash_test<long> t1;
    hash_test<char> t2;
    hash_test<unsigned char> t3;
    
    t1();
    t2();
    t3();
    
    return 0;
}

