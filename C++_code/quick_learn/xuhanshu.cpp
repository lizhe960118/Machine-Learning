# include "stdio.h"
# include "conio.h"

class Parent{
	public:
		char data[20];
		void Function_1();
		virtual void Function_2();
}parent; 

void Parent::Function_1(){
	printf("This is parent function_1\n");
} 

void Parent::Function_2(){
	printf("This is parent function_2\n");
}

class Child:public Parent{
	void Function_1();
	void Function_2();
}child;

void Child::Function_1(){
	printf("This is child function_1\n");
} 

void Child::Function_2(){
	printf("This is child function_2\n");
}

int main(int argc, char* argv[]){
	Parent *p;
	// ��Ϊ���ﶨ����Ǹ����͵�ָ�� 
	if(_getch() == 'c')
		p = &child;
	// ָ����Child�Ķ��� 
	else
		p = &parent;
//		ֱ�����е�ʱ�򣬳���ſ��Ը����û��������жϳ�ָ��ָ��Ķ���
// 		�麯��ʵ����һ������̬���ࡱ�Ĺ��ܣ�������һ�ֶ�̬ 
	p->Function_1();
	p->Function_2();
	return 0;
}
