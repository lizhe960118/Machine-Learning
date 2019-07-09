// node in hashtable
template <class Value> 
struct __hashtable_node{
    __hashtable_node* next;
    Value val;
};

// iterator in hashtable
template <class Value, class Key, class HashFcn, 
          class ExtractKey, class EqualKey, class Alloc> 
struct __hashtable_iterator{
    typedef hashtable<Value, Key, HashFcn, ExtractKey, EqualKey, Alloc> hashtable;
    typedef __hashtable_iterator<Value, Key, HashFcn, ExtractKey, EqualKey, Alloc> iterator;
    typedef __hashtable_const_iterator<Value, Key, HashFcn, ExtractKey, EqualKey, Alloc> const_iterator;    
    typedef __hashtable_node<Value> node;

    typedef forward_iterator_tag iterator_category;
    typedef Value value_type;
    typedef ptrdiff_t different_type;
    typedef size_t size_type;
    typedef Value& reference;
    typedef Value* pointer;

    node* cur;
    hashtable* ht;

    __hashtable_iterator(node* n, hashtable* tab):cur(n), ht(tab);
    __hashtable_iterator(){ }

    reference operator*() const {return cur->val;}
    pointer operator&() const {return &(operator*()); }
    iterator& operator++();
    iterator& operator++(int);

    bool operator==(const iterator& it) const {return cur == it.cur;}
    bool operator!=(const iterator& it) const {return cur != it.cur;}
};

template <class V, class K, class HF, class ExK, class EqK, class A>
__hashtable_iterator<class V, class K, class HF, class ExK, class EqK, class A>&
__hashtable_iterator<class V, class K, class HF, class ExK, class EqL, class A>::operator++{
    const node* old = cur;
    cur = cur->next;
    if(!cur){
        size_type bucket = ht->bkt_num(old_val);
        while(!cur && ++bucket < ht->buckets.size())
            cur = ht->buckets[bucket];
    }
    return *this;
}

template <class V, class K, class HF, class ExK, class EqK, class A> 
inline __hashtable_iterator<class V, class K, class HF, class ExK, class EqK, class A> 
__hashtable_iterator<class V, class K, class HF, class ExK, class EqL, class A>::opeartor++(int){
    iterator tmp = *this;
    ++*this;
    return tmp;
}

template <class Value, class Key, class HashFcn, class ExtractKey, class EqualKey, class Alloc>
class hashtable {
public: 
    typedef HashFcn hasher;
    typedef EqualKey key_equal;
    typedef size_t size_type;
private: 
    hasher hash;
    key_equal equals;
    ExtractKey get_key;

    typedef __hashtable_node<Value> node;
    typedef simple_alloc<node, Alloc> node_allocator;

    vector<node*, Alloc> buckets;
    size_type num_elements;
public:    
    size_type bucket_count() const {return buckets.size();}
}