template <class InputIterator, class Distance> 
void advance_II(InputIterator &i, Distance n){
    while (n--) ++i;
}

template <class BidirectionalIterator, class Distance>
void advance_BI(BidirectionalIterator &i, Distance n){
    if (n > 0){
        while (n--) ++i;
    } else {
        while (n++) ++i;
    }
}

template <class RandomAccessIterator, class Distance> 
void advance_RAI(RandomAccessIterator &i, Distance n){
    i += n;
}

template<class InputIterator, class Distance> 
void advance(InputIterator &i, Distance n){
    if (is_random_access_iterator(i)) advance_RAI(i, n);
    else if (is_bidirectional_iterator(i)) advance_BI(i, n);
    else advance_II(i, n);
} 
// 在执行期间才决定使用哪个版本会影响程序效率 

//5个用作标记的型别
struct input_iterator_tag {};
struct output_iterator_tag {};
struct forward_iterator_tag : public input_iterator_tag {};
struct bidirectional_iterator_tag : public forward_iterator_tag {};
struct random_access_iterator_tag : public bidirectional_iterator_tag {};

// 加入第三参数，使advance函数重载
template <class InputIterator, class Distance> 
inline void __advance(InputIterator &i, Distance n, input_iterator_tag){
    while(n--) ++i;
}

template <class ForwardIterator, class Distance>
inline void __advance(ForwardIterator &i, Distance n, forward_iterator_tag){
    advance(i, n, input_iterator_tag());
}
template <class BidirectionalIterator, class Distance>
inline void __advance(BidirectionalIterator &i, Distance n, bidirectional_iterator_tag){
    if (n > 0){
        while (n--) ++i;
    } else {
        while (n++) ++i;
    }
}

template <class RandomAccessIterator, class Distance> 
inline void __advance(RandomAccessIterator &i, Distance n, random_access_iterator_tag){
    i += n;
}

// 一个对外开放的上层接口, 以算法所能接受的最低阶迭代器型别 template 参数命名
template <class InputIterator, class Distance>
inline void advance(InputIterator &i, Distance n){
    __advance(i, n, iterator_traits<InputIterator>::iterator_category());
}

// iterator_category
/*
template <class I>
inline typename iterator_traits<I>::iterator_category
iterator_category(const I&){
    typename iterator_traits<I>::iterator_category category;
    return iterator_category();
}
*/

template <class I>
struct iterator_traits{
    typedef typename I::iterator_category iterator_category;
};

// 偏特化版本
template <class T>
struct iterator_traits<T*>{
    // 原生指针是一种 Random Access Iterator
    typedef random_access_iterator_tag iterator_category;
};

template <class T>
struct iterator_traits<const T*>{
    typedef random_access_iterator_tag iterator_category;
};


// distance()
template <class InputIterator>
inline iterator_traits<InputIterator>::difference_type
__distance(InputIterator first, InputIterator last, input_iterator_tag){
    iterator_traits<InputIterator>::difference_type n = 0;
    while(first != last){
        ++first;
        ++n;
    }
    return n;
}

template <class RandomAccessIterator>
inline iterator_traits<RandomAccessIterator>::difference_type
__distance(RandomAccessIterator first, RandomAccessIterator last, random_access_iterator_tag){
    return last - first;
}

template <class InputIterator>
inline iterator_traits<InputIterator>::difference_type
distance(InputIterator first, InputIterator last){
    typedef typename iterator_traits<InputIterator>::iterator_category category;
    __distance(first, last, category());
}
