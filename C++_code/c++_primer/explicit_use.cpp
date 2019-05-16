// explicit ???
//example 1
/*
#include <iostream>
using namespace std;

class A{
 public:
    A(int i = 5){
        m_a = i;
    }
 private:
    int m_a;
};

int main(){
    A s;
    s = 10; //??????????int?????A???
    //?A?????????????????????????
    system("pause");
    return 0;
}
*/

//example2
/*
#include <iostream>
using namespace std;

class A{
 public:
    explicit A(int i = 5){
        m_a = i;
    }
 private:
    int m_a;
};

int main(){
    A s;
    s = 10;//  no known conversion for argument 1 from 'int' to 'const A&'
    // s = A(20);
    // cout << s.m_a << endl;
    system("pause");
    return 0;
}

// explicit ????????????
*/

#include <iostream>
using namespace std;

struct A{
    A(int){}
};

int main(){
    A a1(1);
    return 0;
}

