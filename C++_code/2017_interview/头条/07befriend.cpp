#include<iostream>
#include<vector>
#include<set>
#include<algorithm>
using namespace std;

class Solution {
public:
    int earliestAcq(vector<vector<int> >& logs, int N) {
        
        sort(logs.begin(), logs.end(), cmp1); // 日志从小到大排序
        
        vector<set<int> > a;
        set<int> tmp;
        for(int i = 0; i < N; i++){
            tmp.insert(i);
            a.push_back(tmp);
            tmp.clear();
        }
        
        vector<vector<int> >::iterator ite;
        for(ite = logs.begin(); ite != logs.end(); ite++){
            int friend_1 = (*ite)[1];
            int friend_2 = (*ite)[2];
            push_a(a, friend_1, friend_2);
            if(all_friend(a, N)) return (*ite)[0];
        }
        return -1;
    }
    
    void push_a(vector<set<int> >& a, int f1, int f2){
        set<int> result;
        Union(a[f1], a[f2], result);
        set<int> tmp;
        
        tmp = a[f1];
        for(auto c:tmp){
            a[c] = result;
        }
        tmp = a[f2];
        for(auto c:tmp){
            a[c] = result;
        }
        result.clear();
    }
    
    
    void Union(set<int> &A,set<int> &B,set<int> &result){
        set<int>::iterator it;

        it = A.begin();
        while(it != A.end()){
            result.insert(*it);
            it++;
        }

        it = B.begin();
        while(it != B.end()){
            result.insert(*it);
            it++;
        }
    }
    
    static bool cmp1(const vector<int>& a, const vector<int>& b){
        return a[0] < b[0];
    }
    
    static bool all_friend(vector<set<int> > a, int N){
        vector<set<int> >::iterator ite;
        for(ite = a.begin(); ite != a.end(); ite++){
            if(int((*ite).size()) == N) return true;
        }
        return false;
    }
};

int main(){
    int N;
    vector<vector<int> > logs(8);
    N = 6;
    for(int i = 0; i < 8; i++){
        logs[i].resize(3);
    }
    logs[0] = {20190101,0,1};
    logs[1] = {20190104,3,4};
    logs[2] = {20190107,2,3};
    logs[3] = {20190211,1,5};
    logs[4] = {20190224,2,4};
    logs[5] = {20190301,0,3};
    logs[6] = {20190312,1,2};
    logs[7] = {20190322,4,5};
    
    cout << Solution().earliestAcq(logs, N) << endl;
    system("Pause");
    return 0;
}