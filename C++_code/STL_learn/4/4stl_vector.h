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
public: 
    iterator begin(){
        return start;
    }
    iterator end() {
        return finish;
    }
    size_type size() const {
        return size_type(end() - begin());
    }
    size_type capacity() const {
        return size_type(end_of_storage - begin());
    }
    bool empty() const {
        return begin() == end();
    }
    reference operator[](size_type n){
        return *(begin() + n);
    }

    vector():start(0), finish(0), end_of_storage(0){}
    vector(size_type n, const T& value){fill_initialize(n,value);}
    vector(int n, const T& value){fill_initialize(n, value);}
    vector(long n, const T& value){fill_initialize(n, value);}
    explicit vector(size_type n){fill_initialize(n, T());}

    ~vector(){
        destory(start, finish); // 全局函数
        deallocate();
    }

    reference front() {return *begin();}
    reference back() {return *(end() - 1);}
    void push_back(const T& x){ //将元素插入队尾
        if (finish != end_of_storage){
            construct(finish, x); //在最后空指针位置填充x
            ++finish;
        } else {
            insert_aux(end(), x);
        }
    }
    void pop_back() { //将队尾元素取出
        --finish;
        destory(finish);
    }
    iterator erase(iterator position){ //将某一位置元素清除
        if (position + 1 != end()){
            copy(position + 1, finish, position);
        }
        --finish;
        destory(finish);
        return position;
    }
    iterator erase(iterator first, iterator last){
        iterator i = copy(last, finish, first); // 返回最后指向的位置
        destroy(i, finish);
        finish = finish - (last - first);
        return first;
    }
    void resize(size_type new_size, const T& x){
        if (new_size < size()){
            erase(begin() + new_size, end());
        } else {
            insert(end(), new_size - size(), x);
        }
    }
    void resize(size_type new_size){
        resize(new_size, T());
    }
    void clear(){
        erase(begin(), end());
    }

protected:
    iterator allocate_and_fill(size_type n, const T& x){
        iterator result = data_allocator::allocate(n);
        uninitialize_fill_n(result, n, x);
        return result;
    }
};

template <class T, class Alloc>
void vector<T, Alloc>::insert_aux(iterator position, const T& x){
    if (finish != end_of_storage){
        //在备用空间起始处构造一个元素，并以vector最后一个元素作为其初值
        construct(finish, *(finish + 1));
        ++finish;
        T x_copy = x;
        // uninitialized_copy -> (first, last, position)将[first, last)之间的元素，从position开始填充
        copy_backward(position, finish + 2, finish + 1); //(first, last, position)将[first, last)之间的元素，填充到position右边
        *position = x_copy;
    } else { // 没有备用空间
        const size_type old_size = size();
        const size_type len = old_size != 0 ? 2 * old_size : 1;
        
        iterator new_start = data_allocater::allocate(len);
        iterator new_finish = new_start;
        try{
            new_finish = uninitialized_copy(start, position, new_start);
            construct(new_finish, x); // 为新元素设置初值x
            ++new_finish;
            new_finish = uninitialized_copy(position, finish, new_finish); // 插入新position之后的元素
        } catch(...){
            destroy(new_start, new_finish);
            data_allocater::deallocate(new_start, len);
            throw;
        }
        // 析构并释放掉原vector
        destroy(begin(), end());
        deallocate();
        // 调整迭代器，指向新的vector
        start = new_start;
        finish = new_finish;
        end_of_storage = new_start + len;
    }
}
