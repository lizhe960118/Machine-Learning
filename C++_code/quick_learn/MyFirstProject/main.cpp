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
	std::cout << sizeof(a) << endl; // unsigned long he unsigned int ��һ���� 
	std::cout << sizeof(b) << endl;
	std::cout << (numeric_limits<long>::max)() << endl;
	

	c = blue;
	std::cout << c << endl;
	return 0;
}
*/

//1.һ����־����A-Z/a-z/_ ��ʼ�������������߶����ĸ���»��ߣ� ����

/* ����ע�� */
/* c++ ע��
*���Կ���
*/

//2.C++�Ļ����������ͣ�
//�����ͣ�bool), �ַ��ͣ�char), ���ͣ�int), �����ͣ�float), ˫�����ͣ�double), ������void, ���ַ��ͣ�wchar_t)
// һ�������������Ϳ���ʹ��һ�����߶���������η�������
//signed(����)�� unsigned���Ƿ��ţ��� short(�̣���long (���� 

//3. typedef ����
//typedef type newname;
//typedef int my_int; 

//4. ö������
//enum color{ red, green, blue
//} c; 

//����ʹ�� extern ���κεط���������
// ������ֻ����ĳһ�ļ������� �� ����� �ж���һ��

// variable_example
#include <iostream>
using namespace std;

// ��������
extern int a, b;
extern int c;
extern float f;

int main(){
	// �������� 
	int a, b;
	int c;
	float f;
	
	// ��ʼ��
	a = 10;
	b = 20;
	c = a + b;
	f = float(b) / float(c);
	cout << c << endl;
	cout << f << endl;
	return 0;
} 
