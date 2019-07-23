#include<iostream>
#include<vector>


class Solution {
public:
    int minFlipsMonoIncr(string S) {
        int n = S.size();
        // 左右遍历
        vector<int> left(n);
        vector<int> right(n);
        // left表示将S[:i+1]都变成0
        // right表示将S[i:n]都变成1
        left[0] = S[0] - '0';
        right[n-1] = '1' - S[n-1];

        for(int i = 1; i < n; i++){
            left[i] = left[i-1] + (S[i] - '0');
        } 
        for(int i = n-2; i >= 0; i--){
            right[i] = right[i+1] + ('1' - S[i]);
        }
        //遍历一次求最小值
        int ans = right[0];
        for(int i = 1; i < n; i++){
            ans = min(ans, right[i] + left[i-1]);
        }
        ans = min(ans, left[n-1]);
        return ans;
    }
};

class Solution2 {
public:
    int minFlipsMonoIncr(string S) {
        int n = S.size();
        // 构建二维数组，记录转移状态
        // dp[i][0]表示将S[:i+1]都变成0
        // dp[i][1]表示将S[i]=1的合法状态
        vector<vector<int> > dp(n+1, vector<int>(2, 0));
        
        dp[0][0] = S[0] - '0';
        dp[0][1] = 0;

        for(int i = 1; i <= S.size(); i++){
            if (S[i] == '0'){
                dp[i][0] = dp[i-1][0];
                dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + 1;
            }
            else{
                dp[i][0] = dp[i-1][0] + 1;
                dp[i][1] = min(dp[i-1][0], dp[i-1][1]);
            }
        }
          
        return min(dp[n][0], dp[n][1]);
    }
};