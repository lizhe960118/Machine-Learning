#include<iostream>
using namespace std;

/*
int main(){
	int m_value = 1;
	int *p = &m_value;
	cout << p;
	return 0;
}
*/


/* 
//指针的副本传递给方法，原来指针的值不变
 
int m_value = 1;

void func(int *p){
	cout << p << endl;
	// p = pn 
	cout << *p << endl;
	// *p = 2 
	p = &m_value;
}

int main(int argc, char *argv[]){
	int n =2;
	int *pn = &n;
	cout << pn << endl; 
	// pn = 0x6ffe44;
	cout << *pn << endl;
	// *pn = 2;
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
	cout << *p << endl;
	cout << **p << endl;
	*p = &m_value;
//	*p = new int;
//	**p = 5	
} 

int main(int argc, char *argv[]){
	int n = 2;
	int *pn = &n;
	cout << pn << endl;
	cout << *pn << endl;
	func(&pn);
	cout << pn << endl;
	cout << *pn << endl;
	return 0; 
}
*/

//方法二：指针的引用
int m_value = 1;

void func(int *&p){
//	p是指针的引用， main()方法中的 pn 
	cout << p << endl;
	cout << *p << endl;
	p = &m_value;
//	修改p会修改pn的值 
} 

int main(int argc, char *argv[]){
	int n = 2;
	int *pn = &n;
	cout << pn << endl;
	cout << *pn << endl;
	func(pn);
	cout << pn << endl;
	cout << *pn << endl;
	return 0;
} 
