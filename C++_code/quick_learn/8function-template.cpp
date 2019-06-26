#include <iostream>
using std::cout;
using std::endl;

class stone{
public:
    stone():_w(0), _h(0), _weight(0) {}
    stone(int w, int h, int we) : _w(w), _h(h), _weight(we) {}
    
    int get_weight(){
        return _weight;
    }
    bool operator< (const stone& rhs) const {
        return _weight < rhs._weight;
    }

private:
    int _w, _h, _weight;
};

template <class T>
inline 
const T& min(const T& a, const T& b){
    return a < b ? a: b;
}

int main(){
    stone r1(2, 3, 4), r2(3, 3, 5), r3;
    r3 = min(r1, r2); // 编译器会对 function-template 进行参数推导， 确定T为stone
    std::cout << r3.get_weight() << std::endl;
    return 0;
}