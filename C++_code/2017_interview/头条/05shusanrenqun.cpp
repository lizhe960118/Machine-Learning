#include<iostream>
#include<cstring>

using namespace std;

const int N = 100010, M = N * 2; //邻接表

int n; // 树的节点个数

int q[N];
bool st[N];

int h[N], e[M], ne[M], idx; //定义邻接表 
// h表示边的编号， to表示边的终点， ne表示next指针


//链式前向星，h存的是边的编号，ne存的是边的编号
//https://blog.csdn.net/ACdreamers/article/details/16902023
void add(int a, int b){
    e[idx] = b; // add b
    ne[idx] = h[a]; //next指针指向h[a]，表示当前边是以a为起点的边的下一条边
    h[a] = idx; //h[a]存的是以a为顶点的最后一条加入的边
    idx += 1;
}

int dfs(int u, int father) { // 深搜， 传入father防止递归
    int res = 1;
    for (int i = h[u]; ~i; i = ne[i]){ // i表示边
        int son = e[i];
        if(son != father){
            res += dfs(son, u); //u现在是father
        }
    }
    return res;
}

int bfs(int u){ //u表示边的终点，bfs的起点
    int hh = 0, tt =0; // hh表示遍历依次加入的相邻点时的当前点， tt表示加入时的终点
    q[0] = u; 
    st[u] = true; // 存入当前节点
    while(hh <= tt){
        int t = q[hh++]; // 取出一个点
        //计算该点的所有相邻点
        for(int i = h[t]; ~i; i = ne[i]){
            int son = e[i];
            if (!st[son]) { // st[son]=0表示它还没有被访问过
                q[++tt] = son;
                st[son] = true;
            }
        }
    }
    return tt + 1; //尾加1, index + 1,表示点数
}

int main(){
    cin >> n;
    memset(h, -1, sizeof h); // 初始化邻接表， -1表示空指针
    for(int i=0; i < n - 1; i++){
        int a, b;
        cin >> a >> b;
        add(a, b), add(b, a);
    }

    int res = 0;
    for(int i = h[1]; i != -1; i = ne[i]){ // ~i => i != -1
        res = max(res, dfs(e[i], 1)); // e[i]表示边i的终点, 从节点1的子节点开始搜索，并传入节点1，防止循环遍历
    }
    cout << res<< endl;
    return 0;
}