#include <iostream>
#include <assert.h>
using namespace std;

class Rectangle{
public:
    Rectangle(){
        p = new int(100);
    }
    Rectangle(Rectangle &r2){ // 这里传引用是因为传值会再次调用拷贝构造
        height = r2.height;
        width = r2.width;
        p = new int(100); // 这里运行时会在堆里重新分配内存
        *p = (*r2.p);
    }
    ~Rectangle(){
        assert (p != NULL);
        delete p;
    }

private:
    int height;
    int width;
    int *p;
};

int main(){
    Rectangle r1;
    Rectangle r2(r1);
    return 0;
}