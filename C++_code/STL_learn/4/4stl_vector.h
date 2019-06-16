template <class T, class Alloc = alloc> 
class vector{
public: 
    typedef T value_type;
    typedef value_type* pointer;
    typedef value_type* iterator;
    typedef value_type& reference;
    typedef size_t size_type;
    typedef prideff_t difference_type;

protected: 
    typedef simple_alloc<value_type, Alloc> data_allocator;
    iterator start;
    iterator finish;
    iterator end_of_storage; // 目前可用空间的尾

    void insert_aux(iterator position, const T& x);
    void deallocate(){
        if (start){
            data_allocator::deallocate(start, end_of_storage - start);
        }
    }
    void fill_initialize(size_type n, const T& value){
        start = allocate_and_fill(n, value);
        finish = start + n;
        end_of_storage = finish;
    }
};
