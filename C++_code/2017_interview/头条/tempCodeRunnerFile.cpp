#include<bits/stdc++.h>
using namespace std;

typedef long long LL;

int main(){
    int N;
    cin >> N;
    int a[N];
    for (int i = 0; i < N; i++){
        cin >> a[i];
    }
    int M;
    cin >> M;
    LL length_res = N * M;
    LL b[length_res];
    for (int i = 0; i < N; i++){
        for (int j = 0; j < M; j++){
            b[i * N + j] = a[N] / (j + 1);
        }
    }
    sort(b, b + length_res);
    reverse(b, b + length_res);
    cout << b[M];
    return 0;
}