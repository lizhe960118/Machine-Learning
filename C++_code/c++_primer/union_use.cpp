#include <iostream>

union UnionClass{
    UnionClass(): i(10){} // 可含构造函数
    int i;
    double d;
};

static union{ // 全局匿名联合必须是静态的
    int i;
    double d;
};

int main(){
    UnionClass u;
    union{
        int i;
        double d;
    };

    std::cout << u.i << std::endl;

    ::i = 20;
    std::cout << ::i << std::endl;

    i = 30;
    std::cout << i << std::endl; //输出局部匿名联合

    return 0;
}