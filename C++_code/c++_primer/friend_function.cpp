#include <iostream>
using namespace std;

class Circle; //前向声明

class Point{
    friend class Circle;
    friend Point middle(const Point &p1, const Point &p2);
 public:
    Point(float a, float b):x(a), y(b){}
    void print() const{
        cout << x << "," << y << endl;
    }
 private:
    float x;
    float y;
};

Point middle(const Point &p1, const Point &p2){
    Point middel_point((p1.x + p2.x) / 2,(p1.y + p2.y) / 2);
    return middel_point;
}

class Circle{
 public:
    Circle();
    Circle &move(float a, float b);
    void print() const;
 private:
    float radius;
    Point center;
};

Circle::Circle():radius(0.0),center(0.0,0.0){
}

Circle& Circle::move(float a, float b){
    center.x += a;
    center.y += b;
    return *this;
}

void Circle::print() const{
    center.print();
    cout << "radius" << radius << endl;
}

int main(){
    Point p1(1, 1);
    Point p2(2, 2);
    middle(p1, p2).print();

    Circle c;
    c.print();
    c.move(10, 10);
    c.print();
    return 0;
}