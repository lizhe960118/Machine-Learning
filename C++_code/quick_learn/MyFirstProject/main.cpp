#include <iostream>
#include <limits>

using namespace std;
// run this program using the console pauser or add your own getch, system("pause") or input loop 

enum color { red, green=5, blue} c; 

int main() {
	std::cout << "hello world\n";
	
	long int a;
	long long b;
	std::cout << sizeof(a) << endl; // unsigned long he unsigned int 是一样的 
	std::cout << sizeof(b) << endl;
	std::cout << (numeric_limits<long>::max)() << endl;
	

	c = blue;
	std::cout << c << endl;
	
	float k = 0.e55;
	cout << k << endl; 
	
	cout << "hello\tworld\n\n";
	
	short int x;
	short unsigned int y;
	y = 50000;
	x = y;
	
	cout << x << " " << y;
	return 0;
}
