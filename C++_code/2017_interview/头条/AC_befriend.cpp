class Solution {
public:
    int earliestAcq(vector<vector<int>>& logs, int N) {
        
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
            if(push_and_check(a, friend_1, friend_2, N)) return (*ite)[0];
        }
        return -1;
    }
    
    bool push_and_check(vector<set<int> >& a, int f1, int f2, int N){
        set<int> result;
        Union(a[f1], a[f2], result);
        
        if (result.size() == N) return true;
        
        set<int> tmp;
        
        tmp = a[f1];
        for(auto c:tmp){
            a[c] = result;
        }
        tmp = a[f2];
        for(auto c:tmp){
            a[c] = result;
        }
        return false;
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
    
};