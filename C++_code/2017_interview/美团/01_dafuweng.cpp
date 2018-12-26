#include<bits/stdc++.h> 
using namespace std;
/*
//如果跳台阶可以跳1~n中任一一种，则target[n] = 2 * target[n-1] 
f(3) 会有三种跳得方式，1阶、2阶、3阶，那么就是
第一次跳出1阶后面剩下：f(3-1);
第一次跳出2阶，剩下f(3-2)；
第一次3阶，那么剩下f(3-3).
因此结论是 f(3) = f(3-1)+f(3-2)+f(3-3) = f(0) + f(1) + f(2) = 2 * f(2)
f(n) = f(n-1)+f(n-2)+...+f(n-(n-1)) + f(n-n) => 
f(0) + f(1) + f(2) + f(3) + ... + f(n-1) == f(n) = 2*f(n-1)
*/
int jumpHelper(int n){
	if(n <= 0) return -1;
	else if(n == 1) return 1;
	else return 2 * jumpHelper(n -1);
}

	
int main(){
	int n;
	cin >> n;
	int jumpHelper(int n);
	cout << jumpHelper(n) << endl;
	return 0;
}
