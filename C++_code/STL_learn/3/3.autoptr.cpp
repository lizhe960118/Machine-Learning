template<class T>
class auto_ptr{
public:
    explicit auto_ptr(T *p = 0):pointee(p) {} //可以阻止不应该允许的经过转换构造函数进行的隐式转换的发生
    template<class U>
    auto_ptr(auto_ptr<U>& rhs):pointee(rhs.release()) {} //拷贝构造函数
    ~auto_ptr() {delete pointee;}

    template<class U>
    auto_ptr<T>& operator=(auto_ptr<U>& rhs){
        if (this != &rhs) reset(rhs.release());
        return *this;
    }

    T& operator*() const {return *pointee;}
    T* operator-> const {return pointee;} // ->主要用于类类型的指针访问类的成员，而.运算符主要用于类类型的对象访问类的成员。
    T* get() const{return pointee;}

private:
    T *pointee;
}