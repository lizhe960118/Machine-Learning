# 菜鸟 C++

## 1.标志符规范
1个标志符以A-Z/a-z/_ 开始，后面跟零个或者多个字母，下划线， 数字

## 2.注释
```c++
/* 这是注释 */
/* c++ 注释
*可以跨行
*/
```
## 3.C++的基本数据类型：
- 布尔型（bool)
- 字符型（char) 1字节（4bit）
- 整型（int) 4字节 short int 2字节
- 浮点型（float) 4字节
- 双浮点型（double) 6字节
- 无类型void
- 宽字符型（wchar_t) typedef wchar_t short int

一个基本数据类型可以使用一个或者多个类型修饰符来修饰:
- signed(符号)
- unsigned（非符号)
- short(短
- long (长） 

## 4.typedef 声明
```
//typedef type newname;
typedef int my_int; 
```

## 5.枚举类型
```
enum color{ red, green, blue} c; 
```

## 6、变量 
可以使用 extern 在任何地方声明变量, 但变量只能在某一文件，函数或 代码块中定义一次
```
// example_5 
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
```

## 7.常量
### 整数常量 
前缀指定基数：
- 0x， 0X表示十六进制
- 0表示八进制 
- 不带前缀表示十进制
整数常量可以带一个后缀，后缀是U和L的组合

类型 | 是否合法
--|--
212 | 合法
215u | 合法
0xFeeL | 合法
07 | 合法
032UU | 非法
30ul | 无符号长整数

### 浮点常量
浮点常量由整数部分、小数点、小数部分/指数部分组成  
当使用小数形式表示时，必须同时包含整数部分、小数部分  
当使用指数形式表示时，必须同时包含小数点、指数，带符号的指数使用e或者E引入

实例 | 是否合法
--|--
2.112431 | 合法
31413E-5L | 合法
510E | 非法， 不完整的指数
210f | 非法，没有小数或者指数
.e55 | 非法，缺少整数或者分数
 
### 布尔常量
bool

### 字符常量
括在单引号中  
宽字符常量 L'x',必须存储在 wchar_t 类型中
- 普通字符 'x'
- 转义字符 '\t'
- 通用字符 '\u02C0'

### 字符串常量
括在双引号中，可以使用空格做分隔符，将一个很长的字符串常量进行分行
```
"hello, \
dear" = "hello, dear"
```

### 定义常量
#### 使用#define预处理器
```
#define LENGTH 10 // 一般大写
```
#### 使用const关键字
```
// const type variable = value;
const int LENGTH = 10;
```
## 8.修饰符类型
- signed 有符号数 （- 到 +）
- unsigned 无符号数 （0 到 + ）
- long 可应用于双精度型 
- short
c++允许使用速记符号来声明无符号短整数和无符号长整数, int是隐含的  
```
unsigned x;
unsigned int y;
```
## 9.类型限定符 
- const 对象在程序执行期间不能被修改改变
- volatile 告诉编译器不需要优化volatile声明的变量，让程序可以直接从内存中读取变量 ？
- restrict 由 restrict 修饰的指针是唯一一种访问它所指向的对象的方式 ？

## 10.存储类
### static
static存储类指示编译器在程序的生命周期类保持局部变量的存在，而不需要在每次它进入和离开作用域时进行创建和销毁。可以简单理解为定义一次，使用多次。  
static修饰全局变量时，会使变量的作用域限制在它声明的文件内  
static用在类数据成员上时，会导致仅有一个该成员的副本被类的所有对象共享
### extern
extern 用于提供一个全局变量的引用，该全局变量对所有的程序文件都是可见的。可以在本文件中使用extern得到已定义变量或者函数的引用  
```
// main.cpp
#include <iostream>
int count;
extern void write_extern();

int main(){
	count = 5;
	write_extern();
}

// support.cpp
#include <iostream>
extern int count;
void write_extern(void){
	std::cout << "count is "<< count << std::endl;
}
```
### thread_local
使用thread_local声明的变量仅可在其创建的线程上访问，仅可用于数据声明和定义，不可用于函数
```
thread_local int x;

class X
{
 	static thread_local std::string s;
}
static thread_local std::string X::s;

void foo()
{
	thread_local std::vector<int> v; // 本地变量
}
```

## 11. 运算符
### 算数运算符
+、-、*、/、%、++、--
### 关系运算符
==、！=、>、<、>=、<=
### 逻辑运算符
&&、||、！
### 位运算符
&、|、^
### 其他
sizeof、 Condition？X:Y  
& 返回变量的地址、 * 作用在指针上，返回指针指向变量的值  
**指针是一个包含了另一个变量地址的变量**
int &a中的&本质就是“取地址”运算，在函数void swapint(int &a,int &b)中，&a要看成一个整体，看成是x的地址，故a就是x本身了
**定义一个引用的时候，程序把该引用和它的初始值绑定在一起，而不是拷贝它。计算机必须在声明r的同时就要对它初始化，并且，r一经声明，就不可以再和其它对象绑定在一起了。**

## 12.函数
### 函数参数
- 传值调用
- **指针调用** 在函数内，该地址用于访问调用中要用到的实际参数。这意味着，修改形式参数会影响实际参数。
- 引用调用

### lambda表达式
```
[](int x, int y) -> int{ int z = x + y; return z + x;}
```

## 13.数学运算
可能需要引入数学头文件<cmath>
- 随机数 rand()返回一个伪随机数，生成随机数之前必须先调用srand()函数设置种子

## 14.数组
type arrayname [arraysize];

## 15.字符串
### char数组
```
char greeting[6] = {'h', 'e','l','l','o','\0'};
char greeting[] = 'hello';
```
### 提供string类

## 16.指针

## 17.引用
&
### 把引用作为返回值
返回一个指向返回值的隐性指针

## 18.时间和日期

## 19.输入和输出
### 标准输入流
cout 和 流插入运算符 << 结合使用
### 标准输出流
cin 和 流提取运算符 >> 结合使用
### 标准错误流
cerr
### 标准日志流
clog

## 20. 数据结构