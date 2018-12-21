// 语言特性
// 1.初始化方法
int a = 1024
string a = "aaa"
//单引号表示字符变量值，双引号表示字符创 
int a[5] = [0, 1, 2, 3, 4]

int a(1024)
string a("aaa")
int a[5]{0, 1, 2, 3, 4} 
vector<int> iv{1, 2, 3}
map<int, string>{{1,"a"},{2,"b"}}

// 2、类型推测与空指针
//类型推导
auto* p = new Person();

int a = 10;
//类型检测 
decltype(a) b = 20; 

int* p = nullptr;

//3.使用for进行遍历
map<string,int>{{"a", 1},{"b", 2}} 
for(auto p:m){
	cout <<
}
//使用lambda函数，形式为 =-> 函数体
//中括号中等号表示lambda中能范围所有全局变量 
auto func = [=](int& a) -> {return a+10}
//中括号中b,表示lambda中能访问外围b 
auto func = [b](int& a) -> {return a+10}

//4.引用、指针与const
//引用相当于取别名
//指针表示内存地址
const int *p = 10
//常量的指针，*p不能被重新赋值
int a = 100;
int * const p = &a;
//指针常量，标志指针p不能被重新赋值

//5、进制转换
 int a = 10;
 cout << hex << a;
 cout << oct << a;
 cout << bin << a;
 
// 6、字符串和整型之间的转化
#include<sstream>

stringstream ss();
int a = 10;
ss << a;
return ss.str();
