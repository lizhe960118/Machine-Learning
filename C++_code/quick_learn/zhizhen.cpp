#include<iostream>
using namespace std;

/* 
int main(){
	int m_value = 1;
	int *p = &m_value;
	
	cout << &m_value << endl;
	cout << p << endl; // ָ�뱣������һ�����ĵ�ַ 
	cout << *p << endl;
	return 0;
}
*/


//ָ��ĸ������ݸ�������ԭ��ָ���ֵ����
/*
int m_value = 1;

void func(int * p){ //  ������Ҫ�������һ��ָ��int�������ݵ�ָ��p 
	cout << p << endl;
	// p = pn 
	cout << &p << endl;
	cout << *p << endl;
	// *p = 2 
	p = &m_value;
	//ֵ���ݵ��ص��Ǳ����������βε��κβ���������Ϊ�ֲ��������У�����Ӱ������������ʵ�α�����ֵ 
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
	//func�д��ݵ���ʵ��pn�ĸ�����pn����ԭ����ֵ 
	cout << *pn << endl;
	return 0;
}
*/

/*
//����һ��ʹ��ָ���ָ��
int m_value = 1;

void func(int **p){
//	���������Ƕ���p�����ͣ�p��һ��ָ��ָ���ָ�� 
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
//��������ָ�������
int m_value = 1;

void func(int *&p){
//	p��ָ������ã� main()�����е� pn , ��ʱ��ŵ��������������Ž�����ʵ�α����ĵ�ַ��int &a����ʽ��
	cout << p << endl;
	cout << &p << endl; 
	cout << *p << endl;
	p = &m_value;
//	�޸�p���޸�pn��ֵ 
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

