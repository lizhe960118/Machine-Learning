//����c++�������֮��װ��

/* 1��.h��.cpp�ļ� 
//#### Person.h 
//.h �ļ����������Ժͷ��������ƽӿڣ�ֻ���壬��ʵ�֣�
class Person{
private:
	string name;
	int age;
	string gender;
	
public:
	Person();//����
	~Person()//����
	Person(const Person&);//�������캯��
	//��ͬ���͵��������ͨ���������캯����ɸ��Ƶ� 
	string toString();		
}

//#### Person.cpp 
//.cpp�ļ���.h�ļ��ж���ķ�������ʵ��
Person::Person(){
	cout << "���캯��"; 
} 

Person::~Person(){
	cout << "����������ʹ��delete���ͷ��ڴ�"
} 

string Person::toString(){
	return this->name;
} 
*/

/* 2�����캯����ʼ�� 
//���캯����ʵ��ʱ������ͨ����ʼ���б����ĳ�Ա���и�ֵ
//##### Person.h
class Person{
private:
	string _name;
	int _age;
public:
	Person(string name, int age);
	toString();
}

//#### Person.cpp
#include'Person.h'
#include<iostream>
using namespace std;
Person::Person(string name, int age){
	_name(name);
	_age(age);
}

Person p('hk', 10); //��ʼ������ 
*/

//�����ǳ�����Ϳ������캯��
Person p('hk', 10);
Person p_1(p);
auto p_2 = p_1;
//ͨ����ֵ�����纯���Ķ���ͨ��return�ں����з��صĶ��󣬾�����ÿ�������

//�������ж������͵ĳ�Ա������Ҫ�������
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
			_p(x, y); //ʵ����Point���� 
		}
}; 

Line(const Line &cp_line){
	cp_line.count = this -> count;
//	cp_line.p = this -> p; //ֻ��ʵ��ǳ����
	cp_line.p = Point p(this -> x, this -> y); // ��� 
} 
