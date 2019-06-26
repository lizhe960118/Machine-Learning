#include<iostream>
using namespace std;

class Fraction{
public: 
    explicit Fraction(int num, int den = 1):
        m_numerator(num), m_denominator(den){} // one argumnet ctor
    // 不可把3变成 3/1；explicit 清楚的
    operator double() const { // conversion function
        return (double)(m_numerator / m_denominator);
    }
    Fraction operator+(const Fraction& f){
        return Fraction(m_numerator + f.m_numerator, m_denominator + f.m_denominator);
    }

private: 
    int m_numerator;
    int m_denominator;
};

int main(){
    Fraction f(3, 5);
    Fraction d2 = Fraction(f + 4);
    // 可以将 4通过默认构造函数转化为 Fraction, 两个Fraction相加, 加入explicit后，4不会变成fraction
    // 可以把f转成double， double变成int， 和4相加，然后构造d2?
    cout << d2 << endl;
    double d1 = f + 4; // 调用 转换函数将f转成 double
    cout << d1 << endl;

    return 0;
}
