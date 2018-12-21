#include<bits/stdc++.h> 
using namespace std;

set<int> S;
int main(){
	int n;
	scanf("%d",&n);
	for(int i = 0;i < n; i++){
		int x;
		scanf("%d", &x);
		S.insert(x);
	}
	int cnt = 0;
	for(auto &x : S){
		cnt++;
		if(cnt == 3){
			printf("%d", x);
			break;
		}
	}
	if(cnt < 3) printf("-1\n");
	return 0;
}
