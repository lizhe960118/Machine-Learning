#include<bits/stdc++.h>
using namespace std;

const int n = 1000010;//?
char s[n];

int main(){
    int N;
    cin >> N;
    while(N--){ // 对一个字符串处理
        cin >> s;
        int k = 0;
        for(int i = 0; s[i]; i++){
            s[k++] = s[i]; // k表示最后空字符位置
            // 插入的时候，前两字符相同了,处理 AAA
            if (k >= 3 && s[k-1] == s[k-2] && s[k-2] == s[k-3]) {k--;}
            // 处理AABB型
            if (k >= 4 && s[k-1] == s[k-2] && s[k-3] == s[k-4]) {k--;}
        }
        s[k] = '\0';
        cout << s << endl;
    }
     return 0;
}
