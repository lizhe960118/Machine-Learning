// 进制均值 
#include<bits/stdc++.h>
using namespace std;

int hexSum(int n, int a){
	int sum = 0;
	while(n){
		sum += (n % a);
		n = n / a;
	}
	return sum;
} 

int main(){
	int A;
	while(cin>>A){
		int sum = 0;
		for(int i= 2; i <= A - 1;i++){
			sum += hexSum(A, i);
		}
		int r = __gcd(sum, A-2);
		cout << sum / r << '/' << (A-2) / r <<endl;		
	}
	return 0;
}
