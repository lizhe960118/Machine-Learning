#include<bits/stdc++.h>
using namespace std;

int solve(vector<int> data){
	int n = data.size();
	int max_area = 0;
	for(int i =0;i < n;i++){
		int left = 0;
		int right = 0;
		for(;i - left>=0;left++){
			if(data[i - left] < data[i]) break;
		}
		for(;i + right < n;right++){
			if(data[i + right] < data[i]) break;
		}
		int area = data[i] * ((left - 1) + (right - 1) + 1);
		max_area = max(max_area, area);
	}
	return max_area;
}
int main(){
	int n;
	cin >> n;
	vector<int> data;
	for(int i=0; i<n;i++){
		int data_temp;
		cin >> data_temp;
		data.push_back(data_temp);
	}
	int ans = solve(data);
	cout << ans << endl;
	return 0;
} 
