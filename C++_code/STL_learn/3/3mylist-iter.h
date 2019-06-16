#include "3mylist.h"

template <class Item>
struct ListIter{
    Item *ptr; // 提领某一迭代器，换回Item对象
    ListIter(Item *p = 0)
     : ptr(p) {}
    
    Item& operator*() const {return *ptr;}
    Item* operator->() const {return ptr;}

    //前置++
    ListIter operator++() {
        ptr = ptr->next();
        return *this;
    }

    ListIter operator++(int){
        ListIter temp = *this;
        ++*this; // 调用前置++
        return temp;
    }

    bool operator == (const ListIter& i) const{
        return ptr == i.ptr;
    }
    bool operator != (const ListIter& i) const{
        return ptr != i.ptr;
    }
};