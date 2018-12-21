#include<bits/stdc++.h>
using namespace std;

const int nmax = 1000 + 1;
int a[nmax];
int main(){
	int n, m, ans = 0, pos;
	scanf("%d%d", &n, &m);
	for(int i=1; i <= m; i++){
		scanf("%d", &a[i]);
	}
	sort(a + 1, a + 1 + m);
	for(int i=1; i <= m; i++){
//		n是商品数量，m是用户个数 
		if(ans < a[i] * min(n, m - i + 1)){
			ans = a[i] * min(n, m - i + 1);
			pos = i;			
		}
	}
	printf("%d\n",a[pos]);
	return 0;
}
