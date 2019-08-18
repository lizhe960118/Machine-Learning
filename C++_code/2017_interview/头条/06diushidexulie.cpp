#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;

typedef long long  LL;
const LL mod = 998244353;
const int N =1e4+10, M = 210;
int a[N];
LL f[N][M][3], s1[M], s2[M]; // s1为0， 1， 2三个状态前缀和， s2为0， 1前缀和
// f(i,j)表示第i个数为j的方案数之和
//三种状态，f(i,j,0):a(i-1) > a(i) f(i, j, 1):a(i-1) = a(i) f(i, j, 2):a(i-1) < a(i)
//递推关系：从 i - 1转移到 i = > (i-1)有几个状态
// f(i, j, 0) = f(i-1, j+1 ~ 200, 0) + f(i -1, j+1 ~ 200, 1) 减->减， 平->减；不能先增再减，会出现一个数比两边都大
// f(i, j, 1) = f(i-1, j, 0) + f（i-1, j, 1) + f(i-1, j, 2)
// f(i, j, 2) = f(i-1, 0 ~ j-1, 0) + f(i-1, 0 ~ j-1, 1) + f(i-1, 0 ~ j-1, 2) 

int main(){
    int n;
    cin >> n;
    for(int i=0; i < n; i++){
        cin >> a[i];
    }
    //a[1], a[2]给定起点和终点的数值

    //a[1]和a[2]给定的时候，只进行一次初始化，只有两种情况出现
    for(int i =(a[1]? a[1]: 1); i <= (a[1]?a[1]:200); i++){
        for(int j =(a[2]? a[2]: 1); j <= (a[2]?a[2]:200); j++){
            if(i == j) f[2][j][1]++; //从第2个数开始有初始值
            else if (i < j) f[2][j][2]++;
        }
    }


    //  初始化前缀和    
    for(int j = 1; j <=200; j++){
        s1[j] = s1[j-1] + f[2][j][0] + f[2][j][1] + f[2][j][2];
        s2[j] = s2[j-1] + f[2][j][0] + f[2][j][1];
    }

    // 递推
    for (int i=3; i <= n; i++){
        for(int j = (a[i]?a[i]:1); j <=(a[i]?a[i]:200); j++ ){
            f[i][j][0] = (s2[200] - s2[j]) % mod;
            f[i][j][1] = (f[i-1][j][0] + f[i-1][j][1] + f[i-1][j][2]) % mod;
            f[i][j][2] = (s1[j-1]) % mod;
        }

         //  更新前缀和  
        for(int j=1; j<=200; j++){
            s1[j] = s1[j-1] + f[i][j][0] + f[i][j][1] + f[i][j][2];
            s2[j] = s2[j-1] + f[i][j][0] + f[i][j][1];
        }
    }

    LL res = 0;
    for(int j = (a[n]? a[n]:1); j <= (a[n]? a[n]:200); j++){
        res = (res + f[n][j][0] + f[n][j][1]) % mod;
    }

    cout << res << endl;
    return 0;

}