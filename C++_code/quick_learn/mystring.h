#ifndef __MYSTRING__
#define __MYSTRING__

class MyString{
    //big three
public:
    //声明
    MyString(const char* cstr); //构造函数，传入指针
    MyString(const MyString&); //拷贝构造函数, 传入同类对象的引用
    MyString& operator = (const MyString&);//赋值构造函数, 返回同类对象的引用
    ~MyString();//析构函数
    //get_c_str()
    char* get_c_str() {return m_data;}
private:
    char* m_data;
};

#include<string.h>
// MyString::function(){}
inline MyString::MyString(const char* cstr = 0){
    if (cstr){
        m_data = new char[strlen(cstr) + 1]; //分配空间
        strcpy(m_data, cstr); //复制
    } else {
        m_data = new char[1];
        *m_data = '\0';
    }
}

//拷贝构造
inline MyString::MyString(const MyString& rhs){
    m_data = new char[strlen(rhs.m_data) + 1];
    strcpy(m_data, rhs.m_data);
}

//赋值构造
inline
MyString& MyString::operator = (const MyString& rhs){
    if (this == &rhs){
        return *this;
    }
    delete[] m_data;
    m_data = new char[strlen(rhs.m_data) + 1];
    strcpy(m_data, rhs.m_data);
    return *this; //这里还有返回MyString类型的对象
}

// 析构
inline MyString::~MyString(){
    delete[] m_data;
}

// Global-function)(){}

#endif