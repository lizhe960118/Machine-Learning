#include<bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair<int, int> PII;

int main(){
    int N = 100010;
    int bonus[N], scores[N];
    PII person[N]; // 得分，位置
    
    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        for(int i = 0; i < n; i++){
            cin >> scores[i];
            person[i] = {scores[i], i}; 
        }
        sort(person, person + n); // 按照分数给小朋友排序，先算出得分少的
        for(int i = 0; i < n; i++){
            int s = person[i].first, p = person[i].second; // s表示当前得分
            int left = (p - 1 + n) % n, right = (p + 1) % n; // 0映射到n-1, n-1映射到0
            int lv = 1, rv = 1;
            if(s > scores[left]) lv = bonus[left] + 1;
            if(s > scores[right]) rv = bonus[right] + 1;
            bonus[p] = max(lv, rv); // 给第p个人设置的礼物数
        }
        LL res = 0;
        for(int i = 0; i < n; i++){
            res += bonus[i];
        }
        cout << res;
    }
    return 0;
}