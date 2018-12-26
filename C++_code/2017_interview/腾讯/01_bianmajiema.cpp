#include<bits/stdc++.h>
using namespace std;

int factor[] = {25*25*25 + 25*25 + 25 +1, 25*25 + 25 + 1, 25 + 1, 1};

int main(){
	char s[4];
	cin >> s;
	int len = strlen(s);
	int index = len - 1;
	for(int i=0; i< len;i++){
		index += factor[i] * (s[i] - 'a');
	}
	cout << index << endl;
	return 0;
} 
