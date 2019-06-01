template<class T, class Alloc> 
class simple_alloc{
public:
    static T *allocate(size_t n){
        return 0 == n? 0 : (T*)Alloc::allocate(n * sizeof(T));
        // 使得配置器的配置单元从bytes转化为T的特定大小
    }
    static T *allocate(void){
        return (T*)Alloc::allocate(sizeof(T));
    }
    static void deallocate(T *p, size_t n){
        if (0 != n) Alloc::deallocate(n * sizeof(T));
    }
    static void deallocate(T *p){
        Alloc::deallocate(sizeof(T));
    }
    // 四个函数单纯的转调用，调用传递给Alloc（配置器）的成员函数
};

//STL的全部容器都使用这个simple_alloc接口
template <class T, class Alloc = alloc> //缺省使用alloc为配置器
class vector{
protected: 
    typedef simple_alloc<value_type, Alloc> data_allocator;
    void deallocate(){
        if (condition) data_allocator::deallocate(start, end_of_storage - start);
    }
};

// 一级配置器使用 __mallc_alloc_template
template <int inst> 
class __malloc_alloc_template{
private:
    // oom: out of memory
    static void *oom_malloc(size_t);
    static void *oom_realloc(void *, size_t);
    static void (* __malloc_alloc_oom_handler) ();

public:
    static void * allocate(size_t n){
        void *result = malloc(n); // 一级配置器直接使用malloc
        // 如果无法满足调用oom_malloc()
        if (0 == result) result = oom_malloc(n);
        return result;
    }
    static void deallocate(void *p, size_t){
        free(p); // 一级配置器直接使用free
    }
    static void * reallocate(void *p, size_t, size_t new_sz){
        void * result = realloc(p, new_sz);
        if(0 == result) result = oom_realloc(p, new_sz);
        return result;
    }
    // 设置自己的out-of-momery handler
    static void (* set_malloc_handler(void (*f) ())(){
        void (*old) () = __malloc_alloc_oom_handler;
        __malloc_alloc_oom_handler = f;
        return (old);
    };
    //仿真c++的set_net_handler()
};

//客端指定
template <int inst> 
void (* __malloc_alloc_template<inst>::__malloc_alloc_oom_handler) ()= 0;

//设置内存不足处理案例
template <int inst> 
void * __malloc_alloc_template<inst>::oom_alloc(size_t n){
    void (* my_malloc_handler)();
    void *result;
    for(;;){
        my_malloc_handler = __malloc_alloc_oom_handler;
        if (0 == my_malloc_handler) {__THROW_BAD_ALLOC;}
        (*my_malloc_handler)(); //  调用处理程序，企图释放内存
        result = malloc(n);
        if (result) return result;
    }
}

template <int inst> 
void * __malloc_alloc_template<inst>::oom_realloc(void *p, size_t n){
    void (* my_malloc_handler)();
    void *result;
    for(;;){
        my_malloc_handler = __malloc_alloc_oom_handler;
        if (0 == my_malloc_handler) {__THROW_BAD_ALLOC;}
        (*my_malloc_handler)(); //  调用处理程序，企图释放内存
        result = realloc(n); //再次尝试配置内存
        if (result) return result;
    }
}

typedef __malloc_alloc_template<0> malloc_alloc;


