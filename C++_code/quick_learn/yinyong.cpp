#include <iostream>

using namespace std;

double vals[] = {10.1, 12.6, 33.1, 24.1, 50.0};

double& setValues(int i){
	return vals[i];
} 

int main(){
	cout << "value before change" << endl;
	
	for(int i=0; i < 5; i++){
		cout << "vals[" << i << "]=";
		cout << vals[i] << endl;
	}
	
	setValues(1) = 20.23;
//	����������һ������ʱ���򷵻�һ��ָ�򷵻�ֵ����ʽָ��
//���ﷵ����һ��ָ�� vals[1] ����ʽָ�� ��Ȼ����ָ��ָ�� 20.23 
	setValues(2) = 70.8;
	
	cout << "value after change" << endl;
	
	for(int i=0; i < 5; i++){
		cout << "vals[" << i << "]=";
		cout << vals[i] << endl;
	}
	
	return 0;
}
