#include <iostream>
#include <string>
#include <iterator>
#include <vector>
#include <stdlib.h>

using namespace std;

int main(){
    string nums[] = {"one", "two", "three"};
    // string *p = &nums[0];
    // string *p2 = nums;
    // cout << *p << endl;
    // ++p;
    // cout << *p << endl;
    // return 0;
    vector<string> v;
    for (int i = 0; i < sizeof(nums) / sizeof(string); ++i){
        v.push_back(nums[i]);
    }
    vector<string>::iterator begin = v.begin();
    vector<string>::iterator end = v.end();
    for(vector<string>::iterator k = begin; k != end; ++k){
        cout << *k << endl;
    }
    system("Pause");
    return 0;
}