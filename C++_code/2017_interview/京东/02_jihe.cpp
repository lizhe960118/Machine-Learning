#include<bits/stdc++.h>
using namespace std;

set<int> S;
int main(){
	int n, m;
	cin >> n >> m;
	for(int i = 0; i < n; i ++){
		int x;
		cin >> x;
		S.insert(x);
	}
	for(int i = 0; i < m; i ++){
		int x;
		cin >> x;
		S.insert(x);
	}
	for(auto &x : S){
		if(x != *S.rbegin()){
			cout << x << " ";
		}
		else{
			cout << x;
		}
	}
	return 0;
} 
