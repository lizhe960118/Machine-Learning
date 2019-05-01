#include <iostream> 
//#include <stdio.h> 
#include <stdlib.h>
#include <string>
#include <vector>
#include <stack>

using namespace std;

class Solution{
public:
	int evalRPN(vector<string> &tokens){
		stack<int> mystack;
		int n = tokens.size();
			
		for(int i=0; i < n; i++){
			if (isNum(tokens[i])){
				mystack.push(value);
			}
			else if( isOp(tokens[i]) == true){
				if (mystack.size() < 2){
					return 0;
				}
	
				int a = mystack.top();
				mystack.pop();
				int b = mystack.top();
				mystack.pop();
				int c;
				
				if (tokens[i] == "+"){
					c = a + b;
				}
				else if (tokens[i] == "-"){
					c = b - a;
				}
				else if (tokens[i] == "*"){
					c = a * b;
				}
				else if (tokens[i] == "/"){
					c = b / a;
				}
				mystack.push(c);
			}
			else{
				return 0;
			}
		}
			
		if (mystack.size() == 1){
			return mystack.top();	
		} 		
		else{
			return 0;
		}
	}

private:
	long value;
	
	bool isOp(string &op){
		return (op=="+" || op=="-" || op=="*" || op=="/");
	} 
	
	bool isNum(string &num){
		char *end;
		value = strtol(num.c_str(), &end, 10);
		if (end == num.c_str() || *end != '\0'){
			return false;
		}
		return true;
	}
};

int main(){
	Solution s;
    char exps[5][3] = {"42", "9", "6", "-", "+"};
    vector<string> expression;

    cout << "Expression: \n";
    for (int i=0; i<5; i++){
        expression.push_back(exps[i]);
        cout << exps[i] << " ";
    }
    cout << endl;
    cout << s.evalRPN(expression)<<endl;
	return 0;
}
