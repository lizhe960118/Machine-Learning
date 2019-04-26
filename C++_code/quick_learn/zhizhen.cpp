#include<iostream>
using namespace std;

/* 
int main(){
	int m_value = 1;
	int *p = &m_value;
	
	cout << &m_value << endl;
	cout << p << endl; // 指针保存着另一变量的地址 
	cout << *p << endl;
	return 0;
}
*/


//指针的副本传递给方法，原来指针的值不变
/*
int m_value = 1;

void func(int * p){ //  函数需要传入的是一个指向int类型数据的指针p 
	cout << p << endl;
	// p = pn 
	cout << &p << endl;
	cout << *p << endl;
	// *p = 2 
	p = &m_value;
	//值传递的特点是被调函数对形参的任何操作都是作为局部变量进行，不会影响主调函数的实参变量的值 
}

int main(int argc, char *argv[]){
	int n =2;
	int *pn = &n;
	cout << pn << endl; 
	// pn = 0x6ffe44;
	cout << *pn << endl;
	// *pn = 2;
	cout << &pn << endl;
	func(pn);
	//func中传递的其实是pn的副本，pn还是原来的值 
	cout << *pn << endl;
	return 0;
}
*/

/*
//方法一：使用指针的指针
int m_value = 1;

void func(int **p){
//	函数定义是定义p的类型，p是一个指向指针的指针 
	cout << p << endl;
	// 0x6ffe40
	cout << *p << endl;
	cout << **p << endl;
//	*p = &m_value;
	int *new_p = &m_value;
	cout << new_p << endl;
	*p = new_p;
//	*p = new int;
//	**p = 5	
} 

int main(int argc, char *argv[]){
	int n = 2;
	int *pn = &n;
	cout << pn << endl;
	// 0x6ffe4c
	cout << *pn << endl;
	// 2
	func(&pn);
	cout << pn << endl;
	// 0x472010
	cout << *pn << endl;
	// 1
	return 0; 
}
*/

/*
//方法二：指针的引用
int m_value = 1;

void func(int *&p){
//	p是指针的引用， main()方法中的 pn , 这时存放的是由主调函数放进来的实参变量的地址（int &a的形式）
	cout << p << endl;
	cout << &p << endl; 
	cout << *p << endl;
	p = &m_value;
//	修改p会修改pn的值 
} 

int main(int argc, char *argv[]){
	int n = 2;
	int *pn = &n;
	cout << pn << endl;
	cout << *pn << endl;
	cout << &pn << endl;
	func(pn);
	cout << pn << endl;
	cout << *pn << endl;
	return 0;
} 
*/

void swap(int &a, int &b){
	int temp;
	temp = a;
	a = b;
	b = temp;
}
int main(){
	int a, b;
	a = 1;
	b = 2;
	swap(a, b);
	cout << a << endl;
	cout << b << endl;
}

