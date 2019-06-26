template <class T1, class T2>
class Pair{
    typedef T1 first_type;
    typedef T2 second_type;
    T1 first;
    T2 second;
    Pair(): first(T1()), second(T2()){}
    Pair(const T1 &a, const T2& b):first(a), second(b){}

    template <class U1, class U2>
    Pair(const Pair<U1, U2>& p):first(p.first), second(p.second){}
    // 这里要求U1，U2是T1，T2的派生类， 即 U1的对象可以给T1的对象赋值
};