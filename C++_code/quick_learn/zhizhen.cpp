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
//ָ��ĸ������ݸ�������ԭ��ָ���ֵ����
 
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

//��������ָ�������
int m_value = 1;

void func(int *&p){
//	p��ָ������ã� main()�����е� pn 
	cout << p << endl;
	cout << *p << endl;
	p = &m_value;
//	�޸�p���޸�pn��ֵ 
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
