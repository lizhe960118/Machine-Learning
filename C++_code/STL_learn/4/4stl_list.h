template <class T>
struct __list_node{
    typedef void* void_pointer; // 型别为void*，其实可以设为 __list_node<T> *;指向下一个list的节点
    void_pointer prev;
    void_pointer next;
    T data;
}; // 链表的节点

template <class T, class Ref, class Ptr> 
struct __list_iterator{
    typedef __list_iterator<T, T&, T*> iterator;
    typedef __list_iterator<T, Ref, Ptr> self;

    typedef bidireactional_iterator_tag iteartor_category;
    typedef T value_type;
    typedef Ptr pointer;
    typedef Ref reference;
    typedef __list_node<T>* link_type;
    typedef size_t size_type;
    typedef ptrdiff_t difference_type;

    link_type node; //迭代器内部包含一个指向list节点的指针

    //constructor
    __list_iterator(link_type x):node(x) {}
    __list_iterator() {}
    __list_iterator(const iterator& x):node(x.node){}

    bool operator==(const self& x) const {
        return x.node == node;
    }
    bool operator!=(const self& x) const {
        return node != x.node;
    }


    //迭代器取值，取得是节点的数据值
    reference operator*() const {
        return (*node).data;
    }
    pointer operator->() const {
        return &(operator*());
    }

    //迭代器加1
    self& operator++(){
        //  前置++, return前，使迭代器后移 
        node = (link_type)((*node).next);
        return *this;
    }
    self& operator++(int){
        self tmp = *this;
        ++*this;
        return tmp;
    }
    //迭代器减1
    self& operator--(){
        node = (link_type)((*node).prev);
        return *this;
    }
    // *this返回的是当前对象的克隆或者本身（若返回类型为A， 则是克隆， 若返回类型为A&， 则是本身 )
    // this返回当前对象的地址（指向当前对象的指针）
    self& operator--(int){
        self tmp = *this;
        --*this;
        return tmp;
    }  
}; // 链表的迭代器

template <class T, class Alloc = alloc> 
class list {
protected: 
    typedef __list_node<T> list_node;
    typedef __list_iterator<T, T&, T*> iterator;
    typedef list_node& reference;
public:
    typedef list_node* link_type;
protected: 
    link_type node; // 只需要一个指针便可以表示整个链表
    // node 指向 链表尾端刻意设置的空白节点
    iterator begin() {
        return (link_type)((*node).next);
    }
    iterator end() {
        return node;
    }
    bool empty() const {
        return node == node->next;
    }
    size_type size() const {
        size_type result = 0;
        distance(begin(), end(), result);
        return result;
    }
    reference front() {
        return *begin();
    }
    // 取尾节点的内容
    reference back() {
        return *(--end()); // 迭代器向前移动
    }

protected: // 分配空间
    typedef simple_alloc<list_node, Alloc> list_node_allocator;
    // 配置一个节点并回传
    link_type get_node() {
        return list_node_allocator::allocate();
    }
    // 释放一个节点
    void put_node(link_type p) {
        list_node_allocator::deallocate(p);
    }
    // 配置一个带有元素数据的节点
    link_type creat_node(const T& x){
        link_type p = get_node();
        construct(&p->data, x);
        return p;
    }
    // 析构并释放一个节点
    void destroy_node(link_type p){
        destroy(&p->data); // 先释放数据的空间
        put_node(p); // 再释放节点所用的空间
    }

public: //构造函数
    list() { empty_initialize();} // 产生一个空链表
protected:
    void empty_initialize(){
        node = get_node();
        node->next = node;
        node->prev = node;
    }
public: // 链表内部的函数
    void push_back(const T& x){ //将新元素插入list尾端之前
        insert(end(), x);
    }

    iterator insert(iterator position, const T& x){
        link_type tmp = create_node(x);
        // tmp元素的下一个指针指向 cur_node
        // tmp的prev指针指向 cur_node 之前元素；
        tmp->next = position.node;
        tmp->prev = position.node->prev;
        // cur_node之前元素的next指针指向 tmp
        // cur_node的prev指针指向 tmp
        (link_type(position.node->prev))->next = tmp; //这里调用link_type？
        position.node->prev = tmp;
        return tmp;
    }

    void push_front(const T& x){
        insert(begin(), x);
    }
    // 移除position所在节点,返回指向下一个节点迭代器
    iterator erase(iterator position){
        link_type next_node = link_type(position.node->next);
        link_type prev_node = link_type(position.node->prev);
        prev_node->next = next_node;
        next_node->prev = prev_node;
        destroy_node(position.node);
        return iterator(next_node);
    }

    void pop_front(){
        erase(begin());
    }
    void pop_back(){
        iterator tmp = end();
        erase(--tmp);
    }

    // 清除所有节点
    void clear();
    // 将数值为value的节点清除
    void remove(const T& value);
    // 将数值相同的连续元素
    void unique();

    // transfer 将[first, last) 内的所有元素移到position之前
    void transfer(iterator position, iterator first, iterator last){
        if (position != last){
            (*(link_type((*last.node).prev))).next = position.node;
            (*(link_type((*first.node).prev))).next = last.node;
            (*(link_type((*position.node).prev))).next = first.node;
            link_type tmp = link_type((*position.node).prev);
            (*position.node).prev = (*last.node).prev;
            (*last.node).prev = (*first.node).prev;
            (*first.node).prev = tmp;
        }
    }

    // 将x接合于position所指位置之前
    void splice(iterator position, list& x){
        if (!x.empty()){
            transfer(position, x.begin(), x.end());
        }
    }
    // 将i所指元素接合于position所指位置之前
    void splice(iterator position, list&x, iterator i){
        iterator j = i;
        ++j; // i下一个元素所在的迭代器
        if (position == i || position == j) return;
        transfer(position, i, j);
    }
    void splice(iterator position, iterator first, iterator last){
        if (first != last){
            transfer(position, first, last);
        }
    }
    
    // 将x合并到自身，两个list必须是已经排序的
    void merge(list<T, Alloc>&x);
    // 翻转链表
    void reverse();
    // 排序链表
    void sort();
}; // 定义链表结构

template <class T, class Alloc> 
void list<T, Alloc>::clear(){
    link_type cur = (link_type) node->next; // begin()
    while(cur != node){
        link_type tmp = cur;
        cur = (link_type) cur->next;
        destroy_node(tmp);
    }
    node->next = node;
    node->prev = node;
}

template <class T, class Alloc>
void list<T, Alloc>::remove(const T& value){
    iterator first = begin();
    iterator last = end();
    while(first != last){
        iterator next = first;
        ++next;
        if (*first == value){
            erase(first);
        }
        first = next;
    }
}

template <class T, class Alloc>
void list<T, Alloc>::unique(){
    iterator first = begin();
    iterator last = end();
    if (first == last) return;
    iterator next = first;
    while(++next != last){
        if(*first == *next){
            erase(next);
        } else {
            first = next; //调整指针
        }
        next = first; // 修正范围
    }
}

template <class T, class Alloc>
void list<T, Alloc>::merge(list<T, Alloc>&x){
    iterator first1 = begin();
    iterator last1 = end();
    iterator first2 = x.begin();
    iterator last2 = x.end();

    while(first1 != last1 && first2 != last2){
        if (*first2 < *first1){ // 将first2插入到当前位置之前
            iterator next = first2;
            transfer(first1, first2, next++);
            first2 = next;
        } else {
            ++first1;
        }
    }
    if (first2 != last2) transfer(last1, first2, last2);
}

template <class T, class Alloc>
void list<T, Alloc>::reverse(){
    // 链表是否为空或者长度为一
    if (node->next == node || link_type(node->next)->next == node){
        return;
    }
    iterator first = begin();
    iterator last = end();
    ++first;
    while (first != last){
        iterator old = first;
        ++first;
        transfer(begin(), old, first); //将当前元素插入到begin()之前
    }
}

template <class T, class Alloc>
void list<T, Alloc>::sort(){
    if (node->next == node || link_type(node->next)->next == node){
        return;
    }
    list<T, Alloc> carry;
    list<T, Alloc> counter[64];
    int fill = 0;
    while(!empty()){
        carry.splice(carry.begin(), *this, begin());
        int i = 0;
        while(i < fill && !counter[i].empty()){
            counter[i].merge(carry);
            carry.swap(counter[i++]);
        }
        carry.swap(counter[i]);
        if (i == fill) {
            ++fill;
        }
    }
    for (int i = 1; i < fill; ++i){
        counter[i].merge(counter[i-1]);
    }
    swap(counter[fill - 1]);
}