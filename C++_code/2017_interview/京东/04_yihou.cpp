#include<bits/stdc++.h>
using namespace std;
string s;
int n;

//slove把二进制字符串转化成十进制数 
int solve(int n){
	int ans = 0;
	for(int i = 0; i < n; i++){
		ans *= 2;
		ans += s[i] - '0';
	}
	return ans;
} 

int main(){
	scanf("%d", &n);
	cin >> s;
	int a = solve(n);
	cin >> s;
	int b = solve(n);
	printf("%d\n", a ^ b);
	return 0; 
}
