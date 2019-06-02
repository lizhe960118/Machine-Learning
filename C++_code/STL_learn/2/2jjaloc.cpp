#include "2jjaloc.h"
#include <vector>
#include <iostream>
using namespace std;

int main(){
    int ia[5] = {0, 1, 2, 3, 4};
    unsigned int i;

    vector<int, JJ::allocator_test<int> > iv(ia, ia+5);
    for (i=0; i <iv.size(); i++){
        cout << iv[i] << ' ';
    }
    cout << endl;
    system("pause");
    return 0;
}