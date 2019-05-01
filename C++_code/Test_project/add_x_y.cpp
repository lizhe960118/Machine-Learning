#include<iostream>
#include<cstdlib>
#include<ctime>
#include"hello_world.h"
using namespace std;

int main(){
	hello_world();
	int x, y, z;
	srand(time(0));
	x = rand() % 1000;
	y = rand() % 1000;
	cout << x << "+" << y << "=";
	cin >> z;
	while(z != 0){
		while(z != x + y){
			cout << "wrong, do again!\n";
			cout << x << "+" << y << "=";
			cin >> z;
		}
		cout << "right!\n";
		return 0;
	}		
}
