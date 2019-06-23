#include <iostream>
using namespace std;

class Solution {
public:
    int sqrt(int x) {
        int start = 0;
        int end = x;
        long int mid = 0;
        while (start + 1 <= end){
            mid = start + (end - start) / 2;
            if (mid * mid == x) {
                return mid;
            } else if (mid * mid > x) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        if (end * end <= x) return end;
        if (start * start > x) return (start - 1);
        return start;
    }
};

int main(){
    Solution *s = new Solution;
    cout << s->sqrt(2147395599) << endl;
    return 0;
}