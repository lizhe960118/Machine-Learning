#include<bits/stdc++.h>
using namespace std;
const int nmax = 200 + 1;
int a[nmax];

int main(){
	int n;
	scanf("%d", &n);
	for(int i=0; i < n; i++){
		scanf("%d", &a[i]);
	}
	int ans = 800;
//	for(int i=1; i < n-1; i++){
//		int tmp = 0;
//		if(i == 1){
//			int without = abs(a[i+1] - a[i-1]);
//			tmp += without;
//			for(int j=2; j < n - 1; j++){
//				tmp += abs(a[j+1] -a [j]);
//			}
//		}
//		else if(i == n - 2){
//			for(int j = 0; j < n - 3; j++){
//				tmp += abs(a[j+1] -a [j]);
//			}
//			int without = abs(a[i+1] - a[i-1]);
//			tmp += without;
//		}
//		else {
//			for(int j = 0; j < i - 1; j++){
//				tmp += abs(a[j+1] -a [j]);
//			}
//			int without = abs(a[i+1] - a[i-1]);
//			tmp += without;
//			for(int j= i+1 ; j < n-1; j++){
//				tmp += abs(a[j+1] -a [j]);
//			}
//		}
//	
//		if (tmp < ans){
//			ans = tmp;
//		}	
//	}
	for(int i=0; i < n;i++){
		int tmp = 0;
		int last = a[0];
		for(int j = 1; j < n-1; j++){
			if(i == j) continue;
			tmp += abs(a[j] - last);
			last = a[j];
		}
		tmp += abs(a[n-1] - last);
		if (tmp < ans){
			ans = tmp;
		}
	} 
	printf("%d", ans);
	return 0;
} 
