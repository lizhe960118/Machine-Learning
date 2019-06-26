// #include <iostream>
// using namespace std;

// 像一个函数，能接受（）

template <class T1, class T2>
class Pair{
    T1 first;
    T2 second;
    Pair(): first(T1()), second(T2()){}
    // typedef T1 first_type;
    // typedef T2 second_type;
};

template <class Arg, class Result>
struct unary_function {
    typedef Arg argument_type;
    typedef Result result_type;
};

template <class Arg1, class Arg2, class Result>
struct binary_function {
    typedef Arg1 first_argument_type;
    typedef Arg2 second_argument_type;
    typedef Result result_type;
};

template <class T>
struct identity : public unary_function<T, T> {
    const T& operator() (const T& x) const {return x;}
}; // 视为同一个东西

template <class Pair> // 给定一个对象，包含两个元素
struct select1st : public unary_function<Pair, typename Pair::first_type>{
    const typename Pair::first_type& operator() (const Pair&x) const{
        return x.first;
    }
};

template <class Pair>
struct select2nd : public unary_function<Pair, typename Pair::second_type>{
    const typename Pair::second_type& operator() (const Pair& x) const{
        return x.second;
    }
};
