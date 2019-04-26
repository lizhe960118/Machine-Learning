#include <iostream>
#include <ctime>

using namespace std;

/*
int main(){
	time_t now = time(0);
	cout << now << endl;
//	该函数返回系统的当前日历时间，自 1970 年 1 月 1 日以来经过的秒数
	
	char* dt = ctime(&now);
//	返回一个表示当地时间的字符串指针，字符串形式 day month year hours:minutes:seconds year\n\0
	cout << dt << endl;
	
	tm *gmtm = gmtime(&now);
//	函数返回一个指向 time 的指针，time 为 tm 结构
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
