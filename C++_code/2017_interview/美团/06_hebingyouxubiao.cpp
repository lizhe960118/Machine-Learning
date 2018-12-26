#include<bits/stdc++.h> 
using namespace std;

vector<int> sort_list(vector<int> &a, vector<int> &b, int n_c){
	vector<int> c; 
	int n_a = a.size() - 1;
	int n_b = b.size() - 1;
//	printf("%d", n_a);
//	printf("%d", n_b);
	int i = 0,j = 0,k = 0;
	while((i <= n_a) && (j <= n_b)){
		if(a[i] <= b[j]){
			c.push_back(a[i++]);
		}
		else{
			c.push_back(b[j++]);
		}
	}
	while(i != n_a + 1){
		c.push_back(a[i++]);
	}
	while(j != n_b + 1){
		c.push_back(b[j++]);
	}
//	for(int k = 0; k < n_c;k++){
//		cout << c[k];
//	}
	return c;
}

int main(){
	vector<int> a;
	vector<int> b;
	int n_a;
	int n_b;
	cin >> n_a >> n_b;

	for(int i = 0; i<n_a;i++){
		int a_temp;
		cin >> a_temp;
		a.push_back(a_temp);
	}
	for(int i = 0; i<n_b;i++){
		int b_temp;
		cin >> b_temp;
		b.push_back(b_temp);
	}
//	for(int i = 0; i<n_a;i++){
//		cout << a[i];
//	}
//	for(int i = 0; i<n_b;i++){
//		cout << b[i];
//	}
	int n_c = n_a + n_b;
	vector<int> ans = sort_list(a,b,n_c);
    for (int i = 0; i < n_c; i++){
       	cout << ans[i] << endl;
    }
	return 0;
}
