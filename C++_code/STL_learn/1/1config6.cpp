#include <iostream>
using namespace std;

class alloc{
};

template <class T, class Alloc = alloc>
class vector_1{
public: 
    void swap(vector_1<T, Alloc>&){cout << "swap()" << endl;}
};

// #ifdef __STL_FUNCTION_TMPL_PATIAL_ORDER
template <class T, class Alloc> 
inline void swap(vector_1<T, Alloc>& x, vector_1<T, Alloc>& y){
    x.swap(y);
}
// #endif 

int main(){
    vector_1<int> x, y;
    swap(x, y);
    return 0;
}