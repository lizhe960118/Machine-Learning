#include<bits/stdc++.h>
using namespace std;

vector<int> x;

int solve(vector<int> a){
	vector<int> b;
	b = a;
	sort(b.begin(), b.end());
	int p = -1;
	int n = a.size();
	for(int i=0; i < n;i++){
		if(a[i] == b[p+1]){
			p++; 
		}
	}
	return n-(p+1);
} 

int main(){
	int n;
	int x_temp;
	cin >> n;
	for(int i = 0; i < n; i++){
		cin >> x_temp;
		x.push_back(x_temp);
	}
	cout << solve(x) << endl;
	return 0;
}
