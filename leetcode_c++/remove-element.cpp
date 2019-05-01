#include <iostream>

using namespace std;

class Solution {
public:
    int removeElement(int A[], int n, int elem) {
        int left = 0;
        int right = n - 1;
        
        while (left <= right){
            while(right >=0 && A[right] == elem){
                right--;
            }
            
            while(left <= n -1 && A[left] != elem){
                left++;
            }

            cout << left <<right;
            if(left <= right){
                A[left] = A[right];
                A[right] = elem;
            }
        }
        return right + 1;
    }
};

int main(){
//	int A[] = {3, 2, 2, 3};
	int A[] = {1};
	int n = 1;
	int elem = 1;
	
	cout << Solution().removeElement(A, n, elem) << endl;
    system("pause");
	return 0;
} 
