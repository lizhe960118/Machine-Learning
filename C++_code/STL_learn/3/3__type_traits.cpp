// __type_traits用于萃取型别的特性
// 这个型别是否具备 non-trivial defalt ctor?
// 这个型别是否具备 non-trivial copy ctor?
// 这个型别是否具备 non-trivial assignment operator?
// 这个型别是否具备 non-trivial defalt dtor?

// 允许根据不同的型别属性，在编译时完成函数派送决定
template <class ForwardIterator, class Size, class T>
inline ForwardIterator
uninitialized_fill_n(ForwardIterator first, Size n, const T& x){
    return __uninitialized_fill_n(first, n, x, value_type(first));
}

template <class ForwardIterator, class Size, class T, class T1>
inline ForwardIterator
__uninitialized_fill_n(ForwardIterator first, Size n, const T& x){
    typedef typename __type_traits<T1>::is_POD_type is_POD; // 这里萃取 classT1 的 is_POD_type 属性
    return __uninitialized_fill_n_aux(first, n, x, is_POD());
}

template <class ForwardIterator, class Size, Class T>
inline ForwardIterator
__uninitialized_fill_n_aux(ForwardIterator first, Size n, const T& x, __true_type){
    return fill_n(first, n, x);
}

template <class OutputIterator, class Size, class T>
OutputIterator fill_n(OutputIterator first, Size n, T &value){
    for( ; n> 0; --n, ++first){
        *first = value;
    }
    return first;
}

template <class ForwardIterator, class Size, Class T>
inline ForwardIterator
__uninitialized_fill_n_aux(ForwardIterator first, Size n, const T& x, __false_type){
    ForwardIterator cur = first;
    for (; n > 0; --n, ++cur){
        construct(&*cur, x);
    }
    return cur;
}


// __type_traits的定义
struct __true_type {};
struct __false_type {};

template <class type>
struct __type_traits{
    typedef __true_type this_dummy_member_must_be_frist;
    
    typedef __false_type has_trivial_default_constructor;
    typedef __false_type has_trivial_copy_constructor;
    typedef __false_type has_trivial_assignmet_opreator;
    typedef __false_type has_trivial_destructor;
    typedef __false_type is_POD_type;
};

// 对所有的C++标量型别定义 __type_traits的特化版本
// char, signed char, unsigned char
// short, unsigned short,
// int, unsigned int,
// long, unsigned long,
// float,
// double,
// long double
// 这些型别都可以以最快的方式进行拷贝和赋值
__STL_TEMPLATE_NULL struct __type_traits<char> {
    typedef __true_type has_trivial_default_constructor;
    typedef __true_type has_trivial_copy_constructor;
    typedef __true_type has_trivial_assignmet_opreator;
    typedef __true_type has_trivial_destructor;
    typedef __true_type is_POD_type;
}

// 为了效率考虑，在适当情况下选择最合适的手段， copy函数
// 拷贝一个数组，其元素为任意型别
template <class T> 
inline void copy (T* source, T* destination, int n) {
    copy(source, destination, n, typename __type_traits<T>::has_trivial_default_constructor());
}

template <class T> 
void copy (T* source, T* destination, int n, __false_type){
    // 其元素拥有 non-trivial copy constructors
}

template <class T> 
void copy (T* source, T* destination, int n, __true_type){
    // 可借助 memcpy() 完成工作
}

// 对于自定义的型别，未指定，则 __type_traits 萃取出来的都是 __false_type
// 除非特化 __type_traits
template <> 
struct __type_traits<Shape>{
    typedef __true_type has_trivial_default_constructor;
    // 如果 class 有指针类型成员， 并对它进行动态内存分配，则必须实现 has_trivial_xxx; 
    typedef __false_type has_trivial_copy_constructor;
    typedef __false_type has_trivial_assignment_operator;
    typedef __false_type has_trivial_destructor;
    typedef __false_type is_POD_type;
};


