// ��������
// 1.��ʼ������
int a = 1024
string a = "aaa"
//�����ű�ʾ�ַ�����ֵ��˫���ű�ʾ�ַ��� 
int a[5] = [0, 1, 2, 3, 4]

int a(1024)
string a("aaa")
int a[5]{0, 1, 2, 3, 4} 
vector<int> iv{1, 2, 3}
map<int, string>{{1,"a"},{2,"b"}}

// 2�������Ʋ����ָ��
//�����Ƶ�
auto* p = new Person();

int a = 10;
//���ͼ�� 
decltype(a) b = 20; 

int* p = nullptr;

//3.ʹ��for���б���
map<string,int>{{"a", 1},{"b", 2}} 
for(auto p:m){
	cout <<
}
//ʹ��lambda��������ʽΪ =-> ������
//�������еȺű�ʾlambda���ܷ�Χ����ȫ�ֱ��� 
auto func = [=](int& a) -> {return a+10}
//��������b,��ʾlambda���ܷ�����Χb 
auto func = [b](int& a) -> {return a+10}

//4.���á�ָ����const
//�����൱��ȡ����
//ָ���ʾ�ڴ��ַ
const int *p = 10
//������ָ�룬*p���ܱ����¸�ֵ
int a = 100;
int * const p = &a;
//ָ�볣������־ָ��p���ܱ����¸�ֵ

//5������ת��
 int a = 10;
 cout << hex << a;
 cout << oct << a;
 cout << bin << a;
 
// 6���ַ���������֮���ת��
#include<sstream>

stringstream ss();
int a = 10;
ss << a;
return ss.str();
