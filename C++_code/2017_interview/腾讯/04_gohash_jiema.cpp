#include<bits/stdc++.h>
using namespace std;

int main(){
	int left = -90;
	int right = 90;
	char str[6];
	int num;
	cin >> num;
	for(int i=0; i < 6;i++){
		int key = floor((left + right)/2);
		if(num < key){
//			×ó°ë±ß
			right = key;
			str[i] = '0';
		}
		else{
			left = key;
			str[i] = '1';
		}
	}
	cout << str << endl;
	return 0;
} 
