#include<iostream>
#include<vector>
using namespace std;
 
int get_Mth(int a[], int m, int start, int end){ // 得到第m大的数
    if (start > end) return -1;
     
    int left = start;
    int right = end;
    int x = a[start];
    start++;
    while(start <= end){ 
        if (x <= a[start]) start++;
        if (x >= a[end]) end--; // 左边比x大，右边比x小
        if (x < a[end] && x > a[start]){
            int tmp = a[start];
            a[start] = a[end];
            a[end] = tmp;
            start++;
            end--;
        }
    }
    int tmp = a[left];
    a[left] = a[end];
    a[end] = tmp;
     
    if (end == m - 1) return a[end];
    else if (end < m - 1) return get_Mth(a, m, end + 1, right);
    else return get_Mth(a, m, left, end - 1);
}
 
int main(){
    int n = 6;
    int a[6] = {88, 55, 77, 65, 45, 34};
    int m = 3; 
    cout << get_Mth(a, m, 0, n - 1) << endl;
    return 0;
}
