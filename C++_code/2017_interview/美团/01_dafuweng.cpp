#include<bits/stdc++.h> 
using namespace std;
/*
//�����̨�׿�����1~n����һһ�֣���target[n] = 2 * target[n-1] 
f(3) �����������÷�ʽ��1�ס�2�ס�3�ף���ô����
��һ������1�׺���ʣ�£�f(3-1);
��һ������2�ף�ʣ��f(3-2)��
��һ��3�ף���ôʣ��f(3-3).
��˽����� f(3) = f(3-1)+f(3-2)+f(3-3) = f(0) + f(1) + f(2) = 2 * f(2)
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
