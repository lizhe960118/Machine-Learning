//二级配置器 __default_alloc_template
// 每次配置一大块内存，并维持对应之自由链表
// free_list node:
// union obj{
//     union obj * free_list_link; // obj被视为指针，指向实际的区块
//     char client_data[]; 
// };

enum {__ALIGN = 8};
enum {__MAX_BYTES = 128};
enum {__NFREELISTS = __MAX_BYTES / __ALIGN}; // free-lists 个数

template <bool threads, int inst> 
class __default_alloc_template {
private: 
    static size_t ROUND_UP(size_t bytes){
        return (((bytes) + __ALIGN) & ~(__ALIGN - 1));
    }
private: 
    union obj {
        union obj * free_list_link;
        char client_data[1];
    };
private: 
    static obj * volatile free_list[__NFREELISTS];
    // 根据区块大小，决定使用第n号free-list
    static size_t FREE_LIST_INDEX(size_t bytes){
        return  (((bytes) + __ALIGN - 1) / __ALIGN - 1);
    }

    static void *refill(size_t n);
    static char *chunk_alloc(size_t size, int &nobjs);

    static char *start_free;
    static char *end_free;
    static size_t heap_size;

public: 
    static void * allocate(size_t n);
    static void deallocate(void *p, size_t n);
    static void * reallocate( void *p, size_t old_sz, size_t new_sz);
};


// 定义默认数据成员
template <bool threads, int inst> 
char *__default_alloc_template<threads, inst>::start_free = 0;

template <bool threads, int inst> 
char *__default_alloc_template<threads, inst>::end_free = 0;

template <bool threads, int inst> 
size_t __default_alloc_template<threads, inst>::heap_size = 0;

template <bool threads, int inst> 
__default_alloc_template<threads, inst>::obj * volatile 
__default_alloc_template<threads, inst>::free_list[__NFREELISTS] = 
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

//定义 allocate()
static void * allocate (size_t n){
    obj * volatile * my_free_list;
    obj * result;

    //大于最大字节数，调用第一级配置器
    if (n > (size_t) __MAX_BYTES) {
        return (malloc_alloc::allocate(n));
    }

    // 找到16个free-list中适当的一个
    my_free_list = free_list + FREELIST_INDEX(n);
    result = *my_free_list;

    if (result == 0){
        void *r = refill(ROUND_UP(n));
        return r;
    }
    //调整free list
    *my_free_list = result -> free_list_link;
    return (result);
}

//空间释放函数 deallocate()
static void deallocate(void *p, size_t n){
    obj *q = (obj *p);
    obj * volatile * my_free_list;

    if (n > (size_t) __MAX_BYTES){
        malloc_alloc::deallocate(*p, n);
        return;
    }

    my_free_list = free_list + FREELIST_INDEX(n);

    // 调整free list, 回收区块
    q -> free_list = *my_free_list;
    *my_free_list = q;
}

//重新填充 refill()
template <bool threads, int inst> 
void* __default_alloc_template<threads, inst>::refill(size_t n){
    int nobjs = 20;
    char * chunk = chunk_alloc(n, objs);
    obj * volatile * my_free_list;
    obj * result;
    obj * current_obj , * next_obj;

    if (1 == nobjs) return (chunk);

    // 在chunk空间内建立free list
    my_free_list = free_list + FREELIST_INDEX(n);
    result = (obj *) chunk; // 这一块返回给客端
    *my_free_list = next_obj = (obj *)(chunk + n);

    //将free list各个节点连接起来
    for(int i = 1; ; i++){
        current_obj = next_obj;
        next_obj = (obj *)((char *) next_obj + n);
        if (nobjs - 1 == i){
            current_obj -> free_list_link = 0;
        } else {
            current_obj -> free_list_link = next_obj;
        }
    }
    return (result);
}

// 从内存池中取空间给free list
template <bool threads, in inst> 
char * 
__default_alloc_template<thread, inst>::
chunk_alloc(sizt_t size, int* n_objs){
    char * result;
    size_t total_bytes = size * n_objs;
    size_t bytes_left = end_free - start_free;

    if (bytes_left >= total_bytes){
        result = start_free;
        start_free += total_bytes;
        return (result);
    } else if (bytes_left >= size) {
        nobjs = bytes_left / size;
        total_bytes = size * n_objs;
        result = start_free;
        start_free += total_bytes;
        return (result);
    } else {
        size_t bytes_to_get = 2 * total_bytes + ROUND_UP(heap_size >> 4);
        if (bytes_left > 0){
            //内存池还有一些零头，先配给适当的free list;
            obj * volatile * my_free_list = 
                free_list + FREELIST_INDEX(bytes_left);
            ((obj *) start_free) -> free_list_link = * my_free_list;
            *my_free_list = (obj *) start_free;
        }
        //配置 heap 空间，用来补充内存池
        start_free = (char *)malloc(bytes_to_get);
        if (0 == start_free) {
            int i;
            obj * volatile * my_free_list, *p;
            for (i = size; i <= __MAX_BYTES; i += __ALIGN) {
                my_free_list = free_list + FREELIST_INDEX(i);
                p = *my_free_list;
                if (0 != p){ // free list 内尚有未用的区块
                    *my_free_list = p -> free_list_link;
                    start_free = (char *) p;
                    end_free = start_free + i;
                    // 递归调用自己
                    return (chunk_alloc(size, nobjs));
                }
            }
            end_free = 0;
            start_free = (char *)malloc_alloc::allocate(bytes_to_get);
        }
        heap_size += bytes_to_get;
        end_free = start_free + bytes_to_get;
        return (chunk_alloc(size, nobjs));
    }
}