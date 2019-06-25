template <class T, class Ref, class Ptr, class BufSiz> 
struct __deque_iterator
{
    typedef __deque_iterator<T, T&, T*, BufSiz> iterator;
    typedef __deque_iterator<T, Ref, Ptr, BufSiz> const_iterator;
    static size_t buffer_size(){
        return __deque_buf_size(BufSiz, sizeof(T));
    }

    typedef random_access_iterator_tag iteartor_category;
    typedef T value_type;
    typedef Ptr pointer;
    typedef Ref reference;
    typedef size_t size_type;
    typedef ptrdiff_t difference_type;
    typedef T** map_pointer;

    typedef __deque_iterator self;

    T* cur;
    T* first;
    T* last;
    map_pointer node;

    // 需要先分配 new_node 指向的空间
    void set_node(map_pointer new_node){
        node = new_node;
        first = *new_node;
        last = first + difference_type(buffer_size());
    }

    reference operator*() const {return *cur;}
    pointer operator->() const {return &(operator*());}

    difference_type operator- (const self &x)const {
        return difference_type(buffer_size()) * (node - x.node - 1) +
        (cur - first) + (x.last - x.cur);
    } // 求x.cur到当前迭代器cur的距离

    self& operator++() {
        ++cur;
        if (cur == last){
            set_node(node + 1);
            cur = first;
        }
        return *this;
    }

    self& operator++(int){
        self tmp = *this;
        ++*this;
        return tmp;
    }

    self& operator--() {
        if (cur == first){
            set_node(node - 1);
            cur = last;
        }
        --cur;
        return *this;
    }

    self& operator--(int){
        self tmp = *this;
        --*this;
        return tmp;
    }

    self& operator+=(difference_type n){
        difference_type offset = n + (cur - first);
        
        if (offset >= 0 && offset < difference_type(buffer_size())){ // 在同一缓存区中
            cur += n;
        } else {
            difference_type node_offset = offset > 0 ? offset / difference_type(buffer_size()) : -difference_type((-offset-1)/buffer_size()) - 1;
            set_node(node + node_offset);
            cur = first + (offset - node_offset * difference_type(buffer_size());
        }
        return *this;   
    }

    self& operator+(difference_type n){
        self tmp = *this;
        return tmp += n;
    }

    self& operator-=(difference_type n){
        return *this += -n;
    }

    self& operator-(difference_type n){
        self tmp = *this;
        return tmp -= n;
    }

    // 迭代器直接跳过n个距离
    reference operator[](difference_type n){
        return *(*this + n);
    }

    bool operator==(const self& x) const {return cur == x.cur;} //想cur相等，node必须相等
    bool operator!=(const self& x) const {return !(*this == x);}
    bool operator<(const self& x) const {
        return (node == x.node)? (cur < x.cur) : (node < x.node);
    }

};

inline size_t __deque_buf_size(size_t n, size_t sz){
    return n != 0 ? n : (sz < 512? size_t(512 / sz): size_t(1));
}

template <class T, class Alloc = alloc , size_t BufSiz = 0>
class deque
{
public:
    typedef T value_type;
    typedef value_type* pointer;
    typedef value_type& reference;
    typedef ptrdiff_t difference_type;
    typedef size_t size_type;
    typedef __deque_iterator<T,T&, T*, BufSiz> iterator;
protected: 
    typedef pointer* map_pointer;
protected: 
    iterator start;
    iterator finish;
    map_pointer map; // map是块连续空间，每个原属
    size_type map_size; // map 内有多少指针

public:
    iterator begin() {return start;}
    iterator end() {return finish;}

    reference operator[] (size_type n){
        return start[difference_type(n)];
    }

    reference front() {return *start;} // 调用 __deque_iteartor::opreator*
    reference back() {
        iterator tmp = finish;
        --tmp;
        return *tmp;
    }
    size_type size() const {
        return finish - start;;
    }
    size_type max_size() const {return size_type(-1);}
    bool empty() const {return finish == start;}

protected:
    typedef simple_alloc<value_type, Alloc> data_allocator;
    typedef simple_alloc<pointer, Alloc> map_allocator;

    deque(int n, const value_type &value):start(), finist(), map(0), map_size(0){
        fill_initialize(n, value);
    }

public:
    void push_back(const value_type& t){
        if (finish.cur != finish.last - 1){
            construct(finish.cur, t);
            ++finish.cur;
        } else {
            push_back_aux(t);
        }
    }
    void push_front(const value_type& t){
        if (start.cur != start.first){
            construct(start.cur, t);
            --start.cur;
        } else {
            push_front_aux(t);
        }
    }
    void reserve_map_at_back(size_type nodes_to_add = 1){
        if (nodes_to_add + 1 > map_size - (finish.node - map)){
            // 尾部剩余空间不足
            reallocate_map(nodes_to_add, false);
        }
    }
    void reserve_map_at_front(size_type nodes_to_add = 1){
        if (nodes_to_add > start.node - map)){
            // 头部剩余空间不足
            reallocate_map(nodes_to_add, true);
        }
    }

    void pop_back(){
        if (finish.cur != finish.first){
            --finish.cur;
            destroy(finish.cur);
        } else {
            pop_back_aux(t);
        }
    }
    void pop_front(){
        if (start.cur != start.last - 1){
            destroy(start.cur);
            ++start.cur;
        } else {
            pop_front_aux(t);
        }
    }

    iterator erase(iterator position){
        iterator next = position;
        ++next;
        difference_type index = position - start; // 清除点之前的元素
        if (index < (size() / 2)){ // 较少
            // 元素后移
            copy_backward(start, position, next);
            pop_front();
        } else {
            copy(next, finish, position);
            pop_back();
        }
        return start + index;
    }

    iterator insert(iterator position, const value_type& x){
        if (position.cur == start.cur){
            push_front(x);
            return start;
        } else if (position.cur == finish.cur){
            push_back(x);
            iterator tmp = finish;
            --tmp;
            return tmp;
        } else {
            return insert_aux(position, x);
        }
    }
};

template <class T, class Alloc, size_t BufSize>
void deque<T, Alloc, BufSize>::fill_initialize(size_type n, const value_type& value){
    create_map_and_nodes(n);
    map_pointer cur;
    __STL_TRY{
        for (cur = start.node; cur < finish.node; ++cur){
            // 为每个节点设置缓冲区
            uninitialized_fill(*cur, *cur + buffer_size(), value);
        }
        uninitialized_fill(finish.first, finish.cur, value);
    }
    catch(...){

    }
}

template <class T, class Alloc, size_t BufSize>
void deque<T, Alloc, BufSize>::create_map_and_nodes(size_type num_elements){
    // 如果刚好整除，多分配一个节点
    size_type num_nodes = num_elements / buffer_size() + 1；
    // 前后各预留一个，扩充时用
    map_size = max(initial_map_size(), num_nodes + 2);
    map = map_allocator::allocate(map_size);
    map_pointer nstart = map + (map_size - num_nodes) / 2;
    map_pointer nfinish = n_start + num_nodes - 1;
    
    map_pointer cur;
    __STL_TRY{
        for(cur = nstart; cur <= nfinish; ++cur){
            *cur = allocate_node();
        }
    }
    catch(...){

    }
    start.set_node(nstart);
    finish.set_node(nfinish);
    start.cur = start.frist;
    finish.cur = finish.frish + num_elements % buffersize();
}

template <class T, class Alloc, size_t BufSize>
void deque<T, Alloc, BufSize>::push_back_aux(const value_type& t){
    value_type t_copy = t;
    reserve_map_at_back();
    *(finish + 1) = allocate_node();
    __STL_TRY{
        construct(finish.cur, t_copy);
        finish.set_node(finish.node + 1);
        finish.cur = finish.first;
    }
    __STL_UNWIND(deallocate_node(*(finish.node + 1)));
}

template <class T, class Alloc, size_t BufSize>
void deque<T, Alloc, BufSize>::push_front_aux(const value_type& t){
    value_type t_copy = t;
    reserve_map_at_front();
    *(start - 1) = allocate_node();
    __STL_TRY{
        start.set_node(start.node - 1);
        start.cur = start.last - 1;
        construct(start.cur, t_copy);
    }
    catch (...){
        start.set_node(start.node + 1);
        start.cur = start.first;
        deallocate_node(*(start.node - 1));
        throw;
    }
}

template <class T, class Alloc, size_t BufSize>
void deque<T, Alloc, BufSize>::reallocate_map(size_type nodes_to_add, bool add_at_front){
    size_type old_num_nodes = finish.node - start.node + 1;
    size_type new_num_nodes = nodes_to_add + old_num_nodes;

    map_pointer new_nstart;
    if (map_size > 2 * new_num_nodes){
        // 说明分配不当 
        new_nstart = map + (map_size - new_num_nodes) / 2 + (add_at_front? nodes_to_add : 0);
        if (new_nstart < start.node){
            // 说明整体要前移
            copy(start.node, finish.node + 1, new_nstart);
        } else {
            copy_back(start.node, finish.node + 1, new_nstart + new_num_nodes);
        }
    } else {
        // 重新配置map
        size_type new_map_size = map_size + max(map_size + new_num_nodes) + 2;
        map_pointer new_map = map_allocater::allocate(new_map_size);
        new_nstart = new_map + (new_map_size - new_num_nodes) / 2 + (add_at_front? nodes_to_add : 0);
        copy(start.node, finish.node + 1, new_nstart);
        map_allocater::dealloate(map, map_size);
        map = new_map;
        map_size = new_map_size;
    }
    start.set_node(new_nstart);
    finish.set_node(new_nstart + old_num_nodes - 1);//?
}

template <class T, class Alloc, size_t BufSize>
void deque<T, Alloc, BufSize>::pop_back_aux(){ // finish指向空了
    deallocate_node(finish.first);
    finish.set_node(finish.node - 1);
    finish.cur = finish.last - 1;
    destroy(finish.cur);
}

template <class T, class Alloc, size_t BufSize>
void deque<T, Alloc, BufSize>::pop_front_aux(){ // start只用一个元素
    destroy(start.cur);
    deallocate_node(start.first);
    start.set_node(start.node + 1);
    start.cur = start.first;
}

template <class T, class Alloc, size_t BufSize>
void deque<T, Alloc, BufSize>::clear(){
    for (map_pointer node = start.node + 1; node < finish.node; ++node){
        destroy(*node, *node + buffer_size());
        data_allocator::deallocate(*node, buffer_size());
    }
    if (start.node != finish.node){
        destroy(start.cur, start.last);
        destroy(finish.first, finish.cur);
        data_allocator::deallocate(*finish.first, buffer_size());
    } else {
        destroy(start.cur, finish.cur);
    }
    finish = start;
}

template <class T, class Alloc, size_t BufSize>
void deque<T, Alloc, BufSize>::erase(iterator first, iterator last){
    if (first == start && last == finish){
        clear();
        return finish;
    } else {
        difference_type n = last - first;
        difference_type elems_before = first - start; // 清除点前的元素
        if (elems_before < (size() - n) / 2){
            copy_backward(start, first, last);
            iterator new_start = start + n;
            destroy(start, new_start); // 析构冗余元素
            // 释放空间
            for(map_pointer cur = start.node; cur < new_start.node; ++cur){
                date_allocator::deallocate(*cur, *cur + buffer_size());
            }
            start = new_start;
        } else {
            copy(last, finish, first);
            iterator new_finish = finish - n;
            destory(new_finish, finish);
            for(map_pointer cur = new_finish.node + 1; cur < finish.node; ++cur){
                date_allocator::deallocate(*cur, *cur + buffer_size());
            }
            finish = new_finish;
        }
        return new_start + elems_before;
    }
}

template <class T, class Alloc, size_t BufSize>
void deque<T, Alloc, BufSize>::insert_aux(iterator position, const value_type& x){
    difference index = position - start;
    value_type x_copy = x;
    if (index < size() / 2){
        push_front(front());
        iterator front1 = start; // 此时start有更新
        ++front1;
        iterator front2 = front1;
        ++front2;
        position = start + index;
        iterator pos1 = positon;
        ++pos1;
        copy(front2, pos1, front1);
    } else {
        push_back(back());
        iterator back1 = finish;
        --back1;
        iterator back2 = back1;
        --back2;
        position = start + index;
        copy_backward(position, back2, back1);
    }
    *position = x_copy;
    return position;
}