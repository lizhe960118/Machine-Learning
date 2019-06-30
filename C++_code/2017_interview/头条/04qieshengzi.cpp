#include<bits/stdc++.h>
using namespace std;

typedef long long LL;

'''
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
            b[i * M + j] = a[i] / (j + 1); // 假设一段绳子最多切M次
        }
    }
    sort(b, b + length_res); // 找到第M大的，可以用二分
    reverse(b, b + length_res);
    cout << b[M - 1]; // 输出第M大的
    return 0;
}
'''
int n, m;
double a[n];

int main(){
    cin >> n;
    for(int i = 0; i < n; i++) cin >> a[i];
    cin >> m;
    int length = n * n;
    double b[length];
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            double b[i * m + j] = a[i] / (j + 1); // 假设一段绳子最多切M次
        }
    }
    cout << get_Mth(b, m, 0, m * n - 1);
    return 0;
}

// double get_Mth(double a[], int m, int start, int end){ // 得到第m小的数
//     if (start > end) return -1;
    
//     int mid = start + (end - start) >> 1;
//     double x = a[mid];
//     while(start + 1 < end){
//         while ((x < a[end]) && (start + 1 < end)) end--;
//         while ((x >= a[start] && (start + 1 < end)) start++;
//         if(start + 1 < end){
//             double tmp = a[start];
//             a[start] = a[end];
//             a[end] = tmp;
//             start++;
//             end--;
//         }
//     }
//     if (mid == m - 1) return a[mid];
//     else if (mid < m - 1) return get_Mth(a, m - 1 - mid, mid + 1, end);
//     else return get_Mth(a, m, start, mid - 1);
// }


int get_Mth(int a[], int m, int start, int end){ // 得到第m大的数
    if (start > end) return -1;
     
    int left = start;
    int right = end;
    int x = a[start];
    start++;
    while(start <= end){ 
        if (x < a[end] && x > a[start]){
            int tmp = a[start];
            a[start] = a[end];
            a[end] = tmp;
            start++;
            end--;
        }
        if (x <= a[start]) start++;
        if (x >= a[end]) end--; // 左边比x大，右边比x小
    }
    int tmp = a[left];
    a[left] = a[end];
    a[end] = tmp;
     
    if (end == m - 1) return a[end];
    else if (end < m - 1) return get_Mth(a, m, end + 1, right);
    else return get_Mth(a, m, left, end - 1);
}

"""
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int n = nums.size();
        int m = k;
        return get_Mth(nums, m, 0, n - 1);
    }
    
    int get_Mth(vector<int>& a, int m, int start, int end){ // 得到第m大的数
        if (start > end) return -1;

        int left = start;
        int right = end;
        int x = a[start];
        start++;
        while(start <= end){ 
            if (x < a[end] && x > a[start]){
                int tmp = a[start];
                a[start] = a[end];
                a[end] = tmp;
                start++;
                end--;
            }
            if (x <= a[start]) start++;
            if (x >= a[end]) end--; // 左边比x大，右边比x小
        }
        int tmp = a[left];
        a[left] = a[end];
        a[end] = tmp;

        if (end == m - 1) return a[end];
        else if (end < m - 1) return get_Mth(a, m, end + 1, right);
        else return get_Mth(a, m, left, end - 1);
    }

};
"""