# 一、语言特性
## 1.初始化方法
```
int a = 1024
string a = "aaa"
//单引号表示字符变量值，双引号表示字符串
int a[5] = [0, 1, 2, 3, 4]

int a(1024)
string a("aaa")
int a[5]{0, 1, 2, 3, 4} 
vector<int> iv{1, 2, 3}
map<int, string>{{1,"a"},{2,"b"}}
```

## 2、类型推测与空指针
### 类型推导
```
auto* p = new Person();
```
### 类型检测
``` 
int a = 10;
decltype(a) b = 20; 
```
```
int* p = nullptr;
```

## 3.使用for进行遍历
```
map<string,int>{{"a", 1},{"b", 2}} 
for(auto p:m){
	cout << m << endl;
}
```

使用lambda函数，形式为 =-> 函数体
```
//中括号中等号表示lambda中能范围所有全局变量 
auto func = [=](int& a) -> {return a+10}
//中括号中b,表示lambda中能访问外围b 
auto func = [b](int& a) -> {return a+10}
```

## 4.引用、指针与const
引用相当于取别名
指针表示内存地址
```
const int *p = 10
//常量的指针，*p不能被重新赋值
int a = 100;
int * const p = &a;
//指针常量，标志指针p不能被重新赋值
```

## 5、进制转换
``` 
 int a = 10;
 cout << hex << a;
 cout << oct << a;
 cout << bin << a;
```
## 6、字符串和整型之间的转化
```
#include<sstream>

stringstream ss();
int a = 10;
ss << a;
return ss.str();
```

# 二、c++面向对象之封装性
## 1、.h和.cpp文件 
.h 文件负责定义属性和方法（类似接口，只定义，不实现）
```
// #### Person.h 
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
```
.cpp文件对.h文件中定义的方法进行实现
```
//#### Person.cpp 
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
```
## 2、构造函数初始化 
构造函数在实现时，可以通过初始化列表对象的成员进行赋值
```
//##### Person.h
class Person{
private:
	string _name;
	int _age;
public:
	Person(string name, int age);
	toString();
}
```
```
//#### Person.cpp
#include'Person.h'
#include<iostream>
using namespace std;
Person::Person(string name, int age){
	_name(name);
	_age(age);
}

Person p('hk', 10); //初始化对象 
```
## 3.深拷贝，浅拷贝和拷贝构造函数
```
Person p('hk', 10);
Person p_1(p);
auto p_2 = p_1;
//通过传值传递如函数的对象，通过return在函数中返回的对象，均会调用拷贝构造
```
当对象有对象类型的成员，则需要进行深拷贝
```
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
```
# 三、C++面向对象之继承性
## c++中调用父类函数的写法
```
class Person{
	private:
		string _name;
		int _age;
	public:
		Person(string name, int age):_name(name), _age(age){
		}
		void say(){
			cout << "Hello World";
		}
}; 

//继承
class Female:public Person{
	private:
		bool _longhair;
	public:
//		构造函数通过:符号调用父类构造，通过longhair初始化本类参数 
		Female(string name, int age):Person(name, age), _longhair(longhair){
		} 
		void action(){
//			父类的调用，java用super,C#用base,而c++用父类的名字 
			Person::say();
		}
}; 
```