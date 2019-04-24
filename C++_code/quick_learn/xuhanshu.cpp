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
	// 因为这里定义的是父类型的指针 
	if(_getch() == 'c')
		p = &child;
	// 指向类Child的对象 
	else
		p = &parent;
//		直到运行的时候，程序才可以根据用户的输入判断出指针指向的对象
// 		虚函数实现了一个“动态联编”的功能，类似于一种多态 
	p->Function_1();
	p->Function_2();
	return 0;
}
