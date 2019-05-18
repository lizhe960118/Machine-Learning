#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

template <typename T>
class print{
public:
    void operator() (const T& item){
        cout << item << ' ';
    }
};

int main(){
    int ia[6] = {0, 1,2, 3, 4, 5};
    vector<int> v(ia, ia+6);
    for_each(v.begin(), v.end(), print<int>());
    //产生一个临时对象
    return 0;
}