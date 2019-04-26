#include <iostream>

using namespace std;

double vals[] = {10.1, 12.6, 33.1, 24.1, 50.0};

double& setValues(int i){
	return vals[i];
} 

int main(){
	cout << "value before change" << endl;
	
	for(int i=0; i < 5; i++){
		cout << "vals[" << i << "]=";
		cout << vals[i] << endl;
	}
	
	setValues(1) = 20.23;
//	当函数返回一个引用时，则返回一个指向返回值的隐式指针
//这里返回了一个指向 vals[1] 的隐式指针 ，然后让指针指向 20.23 
	setValues(2) = 70.8;
	
	cout << "value after change" << endl;
	
	for(int i=0; i < 5; i++){
		cout << "vals[" << i << "]=";
		cout << vals[i] << endl;
	}
	
	return 0;
}
