#include<bits/stdc++.h>
using namespace std;

bool isPrimeNum(int num){
	if(num < 2) return false;
	for(int i=2; i <num;i++){
		if(num % i == 0) return false;
	}
	return true;
} 

int main(){
	int count = 0;
	int num;
	cin >> num;
	for(int i = 2; i <= num / 2 ;i++){
		if(isPrimeNum(i) && isPrimeNum(num-i)) count++; 
	}
	cout << count << endl;
	return 0;
}
