//二级配置器 __default_alloc_template
// 每次配置一大块内存，并维持对应之自由链表
// free_list node:
union obj{
    union obj * free_list_link; // obj被视为指针，指向实际的区块
    char client_data[]; 
}

//定义 allocate()
//空间释放函数 deallocate()
//重新填充 refill()