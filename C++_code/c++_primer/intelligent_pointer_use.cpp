/*
//1.shared_ptr 
//多个指针指向相同的对象
// 每一个shared_ptr的拷贝都指向相同的内存，每使用一次，内部引用计数加1，每析构一次，内部引用计数减1
#include <iostream>
#include <memory>

int main(){
    int a = 10;
    std::shared_ptr<int> ptra = std::make_shared<int> (a); // 智能指针是一个类
    std::shared_ptr<int> ptra2(ptra); // 拷贝使得对象的引用计数增加一
    std::cout << ptra.use_count() << std::endl; // 2

    int b = 20;
    int *pb = &a;
    std::shared_ptr<int> ptrb = std::make_shared<int> (b);
    ptra2 = ptrb; //赋值使得ptra的引用计数减1，使得ptrb的引用加1
    pb = ptrb.get(); //get获得原始指针

    std::cout << ptra.use_count() << std::endl; // 1
    std::cout << ptrb.use_count() << std::endl; // 2
    std::cout << *pb << std::endl; // 20
    system("pause");
    return 0;
}
*/

/*
//2.unique_ptr
//unique_ptr 唯一拥有其所指向对象，同一时刻只能有一个unique_ptr指向给定对象
#include <iostream>
#include <memory>

int main(){
    {
        std::unique_ptr<int> uptr(new int(10));//绑定动态对象
        // std::unique_ptr<int> uptr2 = uptr;//不能赋值
        // std::unique_ptr<int> uptr2(uptr);//不能拷贝
        std::unqiue_ptr<int> uptr2 = std::move(uptr);//转移所有权
        uptr2.release(); //释放所有权
    }
    //超过uptr的作用域，内存释放
}
*/

/*
//weak_ptr
#include <iostream>
#include <memory>

int main(){
    {
        std::shared_ptr<int> sh_ptr = std::make_shared<int> (10);
        std::cout << sh_ptr.use_count() << std::endl; // 1

        std::weak_ptr<int> wp(sh_ptr);
        std::cout << sh_ptr.use_count() << std::endl; // 1
        std::cout << wp.use_count() << std::endl; // 1
        
        if (!wp.expired()){
            std::shared_ptr<int> sh_ptr2 = wp.lock(); //从被观测的shared_ptr获取一个可用的shared_ptr
            *sh_ptr = 100;
            std::cout << wp.use_count() << std::endl; // 2
        }
    }
    //delete memory
    system("pause");
    return 0;
}
*/
/*
//原始指针
#include <iostream>
#include <memory>

class Child;
class Parent;

class Parent{
private:
    Child *myChild;
public:
    void setChild(Child *ch){
        this->myChild = ch;
    }

    void doSomething(){
        if (this->myChild){
            std::cout << "i already have a child" << std::endl;
        }
    }

    ~Parent(){
        delete myChild;
    }
};

class Child{
private:
    Parent *myParent;
public:
    void setParent(Parent *pa){
        this->myParent = pa;
    }
    void doSomething(){
        if (this->myParent){
            std::cout << "i find my parent" << std::endl;
        }
    }
    ~Child(){
        delete myParent;
    }
};

int main(){
    {
        Parent *pa = new Parent;
        Child *ch = new Child;
        pa->setChild(ch);
        ch->setParent(pa);
        delete ch;
    }
    return 0;
}
*/

/*
//循环引用
#include <iostream>
#include <memory>

class Child;
class Parent;

class Parent{
private:
    // std::shared_ptr<Child> myChild;
    std::weak_ptr<Child> myChild; // weak_ptr对象引用资源是不会增加ch的计数
public:
    void setChild(std::shared_ptr<Child> ch){
        this->myChild = ch;
    }

    void doSomething(){
        if (this->myChild.lock()){//需要访问资源时，weak_ptr调用lock()生成shared_ptr
            std::cout << "i already have a child" << std::endl;
        }
    }

    ~Parent(){
        std::cout << "lose parent" << std::endl;
    }
};

class Child{
private:
    std::shared_ptr<Parent> myParent;
public:
    void setParent(std::shared_ptr<Parent> pa){
        this->myParent = pa;
    }
    void doSomething(){
        if (this->myParent.use_count()){
            std::cout << "i find my parent" << std::endl;
        }
    }
    ~Child(){
        std::cout << "lose child" << std::endl;
    }
};

int main(){
    std::weak_ptr<Parent> wpp;
    std::weak_ptr<Child> wpc;
    {
        std::shared_ptr<Parent> pa(new Parent);
        // 当一个shared_ptr对象要共享这个资源的时候，该资源的引用计数加1，
        // 当这个对象生命期结束的时候，再把该资源引用计数减少1。
        std::shared_ptr<Child> ch(new Child);
        pa->setChild(ch); //不会增加ch的引用计数
        ch->setParent(pa);
        wpp = pa;
        wpc = ch;
        std::cout << pa.use_count() << std::endl; // 2
        std::cout << ch.use_count() << std::endl; // 1
        //指向Child的引用计数为1，先释放
        // Chiid调用析构，则Child类中的myParent被释放，使得pa的引用计数减1
    }
    std::cout << wpp.use_count() << std::endl; // 0
    std::cout << wpc.use_count() << std::endl; // 0
    system("pause");
    return 0;
}
*/

//智能指针的设计和实现
#include <iostream>
#include <memory>

template <typename T>
class SmartPointer{
private:
    T *_ptr;
    size_t *_count;
public:
    SmartPointer(T *ptr = nullptr):_ptr(ptr){
        if(_ptr){
            _count = new size_t(1);
        } else{
            _count = new size_t(0);
        }
    } //默认构造函数

    SmartPointer(const SmartPointer &ptr){
        if (this != &ptr){
            this->_ptr = ptr._ptr;
            this->_count = ptr._count;
            (*this->_count)++; //当前对象的引用计数加1？
        }
    } //拷贝构造函数

    SmartPointer &operator=(const SmartPointer &ptr){
        if (this->_ptr == ptr._ptr){
            return *this;
        }

        if (this->_ptr){ //如果指针已经指向存在的资源
            (*this->_count)--;
            if(this->_count == 0){
                delete this->_ptr;
                delete this->_count;
            }
        }

        this->_ptr = ptr._ptr;
        this->_count = ptr._count;
        (*this->_count)++;
        return *this;
    }//赋值构造函数

    T& operator*(){
        assert(this->_ptr != nullptr);
        return *(this->_ptr);
    }

    T* operator&(){
        assert(this->_ptr != nullptr);
        return this->_ptr;
    }
    ~SmartPointer(){
        (*this->_count)--;
        if (*this->_count == 0){
            delete this->_ptr;
            delete this->_count;
        }
        std::cout << "i leave" << std::endl;
    }
    size_t use_count(){
        return *this->_count;
    }
};

int main(){
    {
        SmartPointer<int> sp(new int(10));
        SmartPointer<int> sp2(sp);
        std::cout << sp.use_count() << std::endl; // 2
        std::cout << sp2.use_count() << std::endl; // 2 => 这里sp2使得其_count指向的地址等于2，sp的_count指向的地址也会等于2

        SmartPointer<int> sp3(new int(30));
        sp2 = sp3;
        std::cout << sp.use_count() << std::endl; // 1
        std::cout << sp2.use_count() << std::endl; // 2
        std::cout << sp3.use_count() << std::endl; // 2
    }
    system("pause");
    return 0;
}