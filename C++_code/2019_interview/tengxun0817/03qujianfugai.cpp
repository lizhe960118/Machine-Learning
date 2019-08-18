//poj1089
#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<vector>

using namespace std;

// #define max_num 0x7fffffff;

typedef long long LL;
int N = 1e5+10;
int L = 1e9+10;

struct node{
    int start;
    int end;
} a[100000 + 10];

int cmp(struct node a, struct node b){
    return a.start < b.start;
}


int main(){
    int n;
    int l; // l is the [0, L]
    cin >> n;
    cin >> l;

    for(int i=0; i <n; i++){
        cin >> a[i].start >> a[i].end;
    }

    vector<struct node> result;

    sort(a, a + n, cmp);

    int ta = a[0].start;
    int tb = a[0].end;
    // a[n].start = max_num;
    // a[n].end = max_num;

    for(int i = 1; i < n; i++){
        if(tb < a[i].start){ // 前一个end小于后面的start
            if(tb + 1 == a[i].start){ //刚好连起
                struct node tmp;
                tmp.start = ta;
                tmp.end = tb;
                result.push_back(tmp);
                ta = a[i].start;
                tb = a[i].end;
            }
            // 不能连起
            cout << -1 << endl;
            return 0;
        }
        else if (tb >= a[i].start ){ // 前一个end大于等于后一个的start，能连起来
            if (tb <= a[i].end){ //前一个end小于等于后一个的end
                tb = a[i].end; // 更新tb
            }
        }
    }
    cout << result.size() << endl;
    return 0;
}