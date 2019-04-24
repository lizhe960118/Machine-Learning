/*
#include <iostream>
#include <limits>

using namespace std;
// run this program using the console pauser or add your own getch, system("pause") or input loop 

enum color { red, green=5, blue} c; 

int main() {
	std::cout << "hello world\n";
	
	long int a;
	long long b;
	std::cout << sizeof(a) << endl; // unsigned long he unsigned int 是一样的 
	std::cout << sizeof(b) << endl;
	std::cout << (numeric_limits<long>::max)() << endl;
	

	c = blue;
	std::cout << c << endl;
	return 0;
}
*/

//1.一个标志符以A-Z/a-z/_ 开始，后面跟零个或者多个字母，下划线， 数字

/* 这是注释 */
/* c++ 注释
*可以跨行
*/

//2.C++的基本数据类型：
//布尔型（bool), 字符型（char), 整型（int), 浮点型（float), 双浮点型（double), 无类型void, 宽字符型（wchar_t)
// 一个基本数据类型可以使用一个或者多个类型修饰符来修饰
//signed(符号)， unsigned（非符号）， short(短），long (长） 

//3. typedef 声明
//typedef type newname;
//typedef int my_int; 

//4. 枚举类型
//enum color{ red, green, blue
//} c; 

//可以使用 extern 在任何地方声明变量
// 但变量只能在某一文件，函数 或 代码块 中定义一次

// variable_example
#include <iostream>
using namespace std;

// 变量声明
extern int a, b;
extern int c;
extern float f;

int main(){
	// 变量定义 
	int a, b;
	int c;
	float f;
	
	// 初始化
	a = 10;
	b = 20;
	c = a + b;
	f = float(b) / float(c);
	cout << c << endl;
	cout << f << endl;
	return 0;
} 
