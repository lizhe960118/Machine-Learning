//32��32λ��unsigned int�������ʾ32*32=1024������ÿ������ÿһλ��ʾһ������ 
#include<bits/stdc++.h>
using namespace std;

int get_task(unsigned int task[32], int b){
	int row, column;
	row = (b-1)/ 32;
	column = (b - 1) % 32;
	unsigned int temp = task[row];
	int status;
//	ȡ����row���޷������ĵ�����columnλ 
	for(int i=0; i <= column; i++){
		status = temp % 2;
		temp /= 2;
	}
	return status;
}

void set_task(unsigned int task[32], int a){
	int row, column;
	row = (a-1) / 32;
	column = (a-1) % 32;
	task[row] += (unsigned int)pow(2, column);
}

int open_task(unsigned int task[32], int a, int b){
	void set_task(unsigned int task[32], int a);
	int get_task(unsigned int task[32], int b);
	if(a < 1 || a > 1024 || b < 1 || b > 1024) return -1;
	if(!get_task(task,a)) set_task(task,a);
	return get_task(task, b);
}
int main(){
	int a,b;
	unsigned int task[32] = {};
	int open_task(unsigned int task[32], int a, int b);
	while(true){
		cin >> a >> b;
		cout << open_task(task, a, b) << endl;
	} 
	return 0;	
} 


