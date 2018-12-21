//二、c++面向对象之封装性

/* 1、.h和.cpp文件 
//#### Person.h 
//.h 文件负责定义属性和方法（类似接口，只定义，不实现）
class Person{
private:
	string name;
	int age;
	string gender;
	
public:
	Person();//构造
	~Person()//析构
	Person(const Person&);//拷贝构造函数
	//相同类型的类对象是通过拷贝构造函数完成复制的 
	string toString();		
}

//#### Person.cpp 
//.cpp文件对.h文件中定义的方法进行实现
Person::Person(){
	cout << "构造函数"; 
} 

Person::~Person(){
	cout << "析构函数，使用delete来释放内存"
} 

string Person::toString(){
	return this->name;
} 
*/

/* 2、构造函数初始化 
//构造函数在实现时，可以通过初始化列表对象的成员进行赋值
//##### Person.h
class Person{
private:
	string _name;
	int _age;
public:
	Person(string name, int age);
	toString();
}

//#### Person.cpp
#include'Person.h'
#include<iostream>
using namespace std;
Person::Person(string name, int age){
	_name(name);
	_age(age);
}

Person p('hk', 10); //初始化对象 
*/

//深拷贝，浅拷贝和拷贝构造函数
Person p('hk', 10);
Person p_1(p);
auto p_2 = p_1;
//通过传值传递如函数的对象，通过return在函数中返回的对象，均会调用拷贝构造

//当对象有对象类型的成员，则需要进行深拷贝
class Point{
	private:
		int _x;
		int _y;
	public:
		Point(int x, int y):_x(x),_y(y){
		}
};
class Line{
	private:
		int _count;
		Point _p;
	public:
		Line(x, y, count):_count(count){
			_p(x, y); //实例化Point对象 
		}
}; 

Line(const Line &cp_line){
	cp_line.count = this -> count;
//	cp_line.p = this -> p; //只能实现浅拷贝
	cp_line.p = Point p(this -> x, this -> y); // 深拷贝 
} 
