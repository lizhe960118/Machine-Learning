#include<bits/stdc++.h>
using namespace std;
char type[51];
double x[51],y[51],z[51];
double mul(double x){
	double ans;
	ans = (x) * (x);
	return ans;		
}

int main(){
	int n;
	scanf("%d", &n);
	for(int i=0; i < n; i++){
		char ch;
		scanf(" %c", &ch);
		type[i]	= ch;
		scanf("%lf", &x[i]);
		scanf("%lf", &y[i]);
		scanf("%lf", &z[i]);
	}
	double ans = 0.0;
	for(int i=0; i < n-2; i++){
		for(int j=i+1; j < n;j++){
			for(int k=j+1; k < n; k++){
				int flag = 0;
				if(type[i] == type[j]) if (type[j] == type[k]) flag = 1;
				if(type[i] != type[j]) if (type[j] != type[k]) if (type[k] != type[i]) flag =1;
				if(flag == 0) continue;
				double uy = y[j] - y[i];
				double ux = x[j] - x[i], uz = z[j] - z[i];
				double vx = x[k] - x[i], vy = y[k] - y[i], vz = z[k] - z[i];
				double area = sqrt(mul(ux*vy - vx * uy) + mul(uy*vz - uz*vy) + mul(uz*vx - vz*ux));
				area *= 0.5;
				ans = max(ans, area); 
			}
		}
	}
	printf("%.5lf\n", ans);
	return 0;
} 
