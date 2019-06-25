#include<iostream>
#include<deque>
#include<algorithm>
using namespace std; 

int main(){
    deque<int> ideq(20, 9);
    cout << "size=" << ideq.size() << endl;
    
    for(int i= 0; i < ideq.size(); ++i){
        ideq[i] = i;
    }

    for(int i=0; i < ideq.size(); ++i){
        cout << ideq[i] << " ";
    }
    cout << endl;

    for(int i=0; i < 3; ++i){
        ideq.push_back(i);
    }
    for(int i=0; i < ideq.size(); ++i){
        cout << ideq[i] << " ";
    }
    cout << endl;

    ideq.push_back(3);
    ideq.push_front(99);
    for(int i=0; i < ideq.size(); ++i){
        cout << ideq[i] << " ";
    }
    cout << endl;
    cout << "size=" << ideq.size() << endl;

    ideq.push_front(98);
    ideq.push_front(97);
    deque<int>::iterator ite;
    ite = find(ideq.begin(), ideq.end(), 99);
    cout << *ite << endl;
    // cout << *(ite.cur) << endl;
}