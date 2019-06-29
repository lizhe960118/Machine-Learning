//Z国的货币系统包含面值1元、4元、16元、64元共计4种硬币，以及面值1024元的纸币，现在小Y使
//用1024元的纸币购买力一种价值为N(0<N<1024)的商品，请问最少他会收到多少硬币？

#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    n = 1024 - n; //求出剩余值,现在有n元，要找零
    int dp[n + 1];// 保存最后结果

    if (n <= 0){
        cout << 0;
    } else if (n == 1) {
        cout << 1;
    } else if (n == 4) {
        cout << 1;
    } else if (n == 16) {
        cout << 1;
    } else if (n == 64) {
        cout << 1;
    } else if (n == 2) {
        cout << 2;
    } else if (n == 3){
        cout << 3;
    } else { // n > 4
        // dp初始化
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 3;
        dp[4] = 1;
        for(int i = 4; i < n + 2; i++) {
            if (i == 16 || i == 64){
                dp[i] = 1;
            } else if (i > 4 && i < 16) {
                dp[i] = min(dp[i - 1], dp[i - 4]) + 1;
            } else if (i > 16 && i < 64) {
                // dp递推
                dp[i] = min(min (dp[i - 1], dp[i - 4]), dp[i - 16]) + 1;
            } else {
                dp[i] = min( min ( min (dp[i - 1], dp[i - 4]) , dp[i - 16]) , dp[i - 64]) + 1;
            }
        }
        cout << dp[n];
    }
    
    system("pause");
    return 0;
}