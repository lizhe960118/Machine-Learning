#ifndef __COMPLEX__
#define __COMPLEX__

#include <cmath>

class ostream;
class complex;

complex& __doapl(complex* ths, const complex& r);

class complex{  //class head
//class body
public:
    complex (double r = 0, double i = 0):re(r), im(i){} // 构造函数
    double real() const {return re;}
    double imag() const {return im;}
    // 以上三个函数在本体内定义，便成为inline候选人
    //函数声明
    complex& operator += (const complex&);
private:
    double re, im;

    friend complex& __doapl(complex *, const complex& r);
    // do assignment plus 函数可以直接访问r的私有变量
};
// 可以使用模板替换到double

/*
template <class T>
class complex{
public:
    complex (T r = 0, T i = 0):re(r), im(i){}
private:
    T re, im;
}
使用：
complex<double> c1(2.5, 1.5);
complex<int> c2(2, 1);
*/
inline complex& 
__doapl(complex* ths, const complex& r){
    ths->re += r.re; // this是关键字，不能直接使用
    ths->im += r.im;
    return *ths;
}

// complex::function(){} 类中函数的实现
inline complex& //返回引用是为了连加实现
complex::operator += (const complex& r){
    return __doapl(this, r); // this指代操作符左边的对象
}

//定义全域函数
inline double 
imag (const complex& r){
    return r.imag();
}
inline double
real (const complex& r){
    return r.real();
}
//使用：
// complex c(2, 1);
// cout << imag(c);

//重载+号
inline complex 
operator + (const complex& x, const complex& y){
    return complex( real(x) + real(y),
                    imag(x) + imag(y));
    // 因为返回的需要是local object,不能return by reference
}
inline complex 
operator + (const complex& x, double y){
    return complex( real(x) + y, imag(x));
}
inline complex 
operator + (double x, const complex& y){
    return complex( x + real(y), imag(y));
}

//重载+，-号
inline complex 
operator + (const complex& x){
    return x;
}
inline complex
operator - (const complex& x){
    return complex(-real(x), -imag(x));
}

//重载 ==, 返回bool类型的值
inline bool
operator == (const complex& x, const complex& y){
    return (real(x) == real(y) && imag(x) == imag(y));
}
inline bool 
operator == (const complex& x, double y){
    return (real(x) == y && imag(x) == 0);
}
inline bool
operator == (double x, const complex& y){
    return (x == real(y) && imag(y) == 0);
}

//重载 ！=
inline bool
operator != (const complex& x, const complex& y){
    return (real(x) != real(y) || imag(x) != imag(y));
}
inline bool 
operator != (const complex& x, double y){
    return (real(x) != y || imag(x) != 0);
}
inline bool
operator != (double x, const complex& y){
    return (x != real(y) && imag(y) != 0);
}

//共轭复数 conj
inline complex 
conj (const complex& r){
    return complex(real(r), -imag(r));
}

//输出字符 <<
#include <iostream>

std::ostream&
operator << (std::ostream& os, const complex& r){
    os << '(' << real(r) << ',' << imag(r) << ')';
    return os;
}

#endif