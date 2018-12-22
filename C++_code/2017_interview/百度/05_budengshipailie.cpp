#include<bits/stdc++.h>
using namespace std;

int dp[1000][1000];

int main(){
	int n, k;
	cin >> n >> k;
	for(int i = 1; i<=n;i++){
		dp[i][0] = 1;
	}
	for(int i=2;i<=n;i++){
		for(int j=1;j<=k;j++){
			dp[i][j] = (dp[i-1][j-1] * (i-j) + dp[i-1][j] * (j+1)) % 2017;
		}
	}
	cout << dp[n][k] << endl;
	return 0;
} 
