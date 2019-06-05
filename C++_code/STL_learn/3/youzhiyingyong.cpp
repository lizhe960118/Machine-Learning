#include <iostream>
using namespace std;

int getdata(int &&num)
{
cout << num << endl;
num += 10;
return num;
}


int main()
{
int a = 5;
cout << getdata(a + 1) << endl; //传入的a+1为寄存器中的值，是为右值
return 0;
}