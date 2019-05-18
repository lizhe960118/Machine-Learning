#include <iostream>
using namespace std;

template <class InputIterator, class T>
InputIterator find(InputIterator first, InputIterator last, const T& value){
    while(first != last && *first != value) ++first;
    return first;
};

template <class InputIterator, class Function>
Function for_each(InputIterator first, InputIterator last, Function f){
    for(;first != last; ++first)
        f(*first);
    return f;
}