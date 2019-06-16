#include <iostream>
#include <vector>
#include <deque>
#include <list>
#include <algorithm>

using namespace std;

int main(){
    const int array_size = 7;
    int ia[array_size] = {0, 1, 2, 3, 4, 5, 6};

    vector<int> ivect(ia, ia + array_size);
    deque<int> ideque(ia, ia + array_size);
    list<int> ilist(ia, ia + array_size);

    vector<int>::iterator it1 = find(ivect.begin(), ivect.end(), 4);
    if (it1 != ivect.end()){
        cout << "4 is found in " << *it1 << endl;
    } else {
        cout << "4 is not found" << endl;
    }

    deque<int>::iterator it2 = find(ideque.begin(), ideque.end(), 6);
    if (it2 != ideque.end()){
        cout << "6 is found in " << *it2 << endl;
    } else {
        cout << "5 is not found" << endl;
    }

    list<int>::iterator it3 = find(ilist.begin(), ilist.end(), 8);
    if (it3 != ilist.end()){
        cout << "8 is found in " << *it3 << endl;
    } else {
        cout << "8 is not found" << endl;
    }

    return 0;
}