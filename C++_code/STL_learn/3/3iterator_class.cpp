// iterator class 
template <class Category, 
          class T,
          class Distance = ptrdiff_t,
          class Pointer = T*,
          class Reference = T&>
struct iterator {
    typedef Category iterator_category;
    typedef T value_type;
    typedef Distance difference_type;
    typedef Pointer pointer;
    typedef Reference reference;
};

// 设计适当的相应型别是迭代器的责任
template <class Item>
struct ListIter:
    public std::iterator<std::forward_iteratro_tag, Item>{
};

//设计适当的迭代器是容器的责任
//唯容器本身，才知道应该设计出增养的迭代器来遍历自己

//算法：独立于容器和迭代器，设计时以迭代器为对外接口即可