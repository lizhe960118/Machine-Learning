#include<bits/stdc++.h>
using namespace std;

const int maxn = 100 + 5;
int n, a[maxn];
//dp[i][j]表示前i个题目答对j道 
//dp[i][j] = dp[i-1][j] * 当前答错 + dp[i-1][j-1] * 当前答对 
double dp[maxn][maxn];

int main(){
	scanf("%d", &n);
	for(int i = 1; i < n; i++) scanf("%d", &a[i]);
	dp[0][0] = 1;
	for(int i = 1; i <= n; i++){
		dp[i][0] = dp[i-1][0] * (100.0 - a[i]) / 100;
		for(int j = 1; j <= i; j++){
			dp[i][j] = dp[i-1][j] * (100.0 -a[i]) / 100 + dp[i-1][j-1] * 1.0 * a[i] / 100;
		}
	}
	int begin = (3 * n + 4) / 5; //至少答对60%题目才算通过 
	double ans = 0;
	for(int i = begin; i <= n; i++) ans += dp[n][i];
	printf("%.5f\n", ans); 
	return 0; 
}
