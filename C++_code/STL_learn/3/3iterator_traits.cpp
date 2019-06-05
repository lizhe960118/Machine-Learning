//用于萃取迭代器的特性 
template <class Iterator>
struct iterator_traits{ 
    typedef typename Iterator::iterator_category iterator_category;
    typedef typename Iterator::value_type        value_type;
    typedef typename Iterator::difference_type   difference_type;
    typedef typename Iterator::pointer_type      pointer_type;
    typedef typename Iterator::reference_type    reference_type;
};

template <class T>
struct iterator_traits<T*>{
    typedef random_access_iterator_tag iterator_category;
    typedef T                          value_type;
    typedef ptrdiff_t                  difference_type;
    typedef T*                         pointer_type;
    typedef T&                         reference_type;
};

template <class T>
struct iterator_traits<const T*>{
    typedef random_access_iterator_tag iterator_category;
    typedef T                          value_type;
    typedef ptrdiff_t                  difference_type;
    typedef const T*                   pointer_type;
    typedef const T&                   reference_type;
};