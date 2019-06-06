//将内存配置和对象构造分离开
// uninitialized_copy()
//在[result, result + (last - first))区域内，给[first, last)范围内的每一个对象复制一个样本
template <class InputIterator, class ForwardIterator>
inline ForwardIterator
uninitialized_copy(InputIterator first, InputIterator last, ForwardIterator result){
    return __uninitialized_copy(first, last, result, value_type(result));
}
template <class InputIterator, class ForwardIterator, class T>
inline ForwardIterator
__uninitialized_copy(InputIterator first, InputIterator last,
                     ForwardIterator result, T*){
    typedef typename __type_traits<T>::is_POD_type is_POD;
    return __uninitialized_copy_aux(first, last, result, is_POD());
    // 让编译器做参数推导
}

template <class InputIterator, class ForwardIterator>
inline ForwardIterator
__uninitialized_copy_aux(InputIterator first, InputIterator last,
                     ForwardIterator result, __true_type){
    return copy(first, last, result);
}

template <class InputIterator, class ForwardIterator>
inline ForwardIterator
__uninitialized_copy_aux(InputIterator first, InputIterator last,
                     ForwardIterator result, __false_type){
    ForwardIterator cur = result;
    for (; first != last; ++first, ++cur){
        construct(&*cur, *first);
    }
    return cur;
}

/********************/
// uninitialized_fill() 从first到last填充x
template <class ForwardIterator, class T>
inline void 
uninitialized_fill(ForwardIterator first, ForwardIterator last, const T&x){
    return __uninitialized_fill(first, last, x, value_type(first));
}

template <class ForwardIterator, class T, class T1>
inline void 
__uninitialized_fill(ForwardIterator first, ForwardIterator last, const T&x, T1*){
    typedef typename __type_traits<T1>::is_POD_type is_POD;
    return __uninitialized_fill_aux(first, last, x, isPOD());
}

template <class ForwardIterator, class T>
inline void 
__uninitialized_fill(ForwardIterator first, ForwardIterator last, const T&x, __true_type){
    fill(first, last, x); 
}

template <class ForwardIterator, class T>
inline void 
__uninitialized_fill(ForwardIterator first, ForwardIterator last, const T&x, __false_type){
    ForwardIterator cur = first;
    for(; cur != last; ++cur){
        construct(&*cur, x);
    }
}

/************/
// uninitialized_fill_n() 从first开始以x填充n
template <class ForwardIterator, class Size, class T>
inline ForwardIterator
uninitialized_fill_n(ForwardIterator first, Size n, const T& x){
    return __uninitialized_fill_n(first, n, x, value_type(first));
}

template <class ForwardIterator, class Size, class T, class T1>
inline ForwardIterator
__uninitialized_fill_n(ForwardIterator first, Size n, const T& x){
    typedef typename __type_traits<T1>::is_POD_type is_POD;
    return __uninitialized_fill_n_aux(first, n, x, is_POD());
}

template <class ForwardIterator, class Size, Class T>
inline ForwardIterator
__uninitialized_fill_n_aux(ForwardIterator first, Size n, const T& x, __true_type){
    return fill_n(first, n, x);
}

template <class ForwardIterator, class Size, Class T>
inline ForwardIterator
__uninitialized_fill_n_aux(ForwardIterator first, Size n, const T& x, __false_type){
    ForwardIterator cur = result;
    for (; n > 0; --n, ++cur){
        construct(&*cur, x);
    }
    return cur;
}


