#include <iostream>
#include <ctime>

using namespace std;

/*
int main(){
	time_t now = time(0);
	cout << now << endl;
//	�ú�������ϵͳ�ĵ�ǰ����ʱ�䣬�� 1970 �� 1 �� 1 ����������������
	
	char* dt = ctime(&now);
//	����һ����ʾ����ʱ����ַ���ָ�룬�ַ�����ʽ day month year hours:minutes:seconds year\n\0
	cout << dt << endl;
	
	tm *gmtm = gmtime(&now);
//	��������һ��ָ�� time ��ָ�룬time Ϊ tm �ṹ
//	cout << *gmtm << endl;
	dt = asctime(gmtm);
	cout << dt << endl;
	return 0;
} 
*/

int main(){
	time_t now = time(0);
	
	cout << now << endl;
	
	tm *ltm = localtime(&now);
	
	cout << "year" << 1900 + ltm->tm_year << endl;
	cout << "month" << 1 + ltm->tm_mon << endl;
	cout << "time" << ltm->tm_hour << ":" << ltm->tm_min  << ":" << ltm->tm_sec <<endl;
}
