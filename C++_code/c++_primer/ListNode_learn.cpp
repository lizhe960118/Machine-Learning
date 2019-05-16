#include <iostream>
using namespace std;

struct ListNode{
    int val;
    ListNode* next;
};

class Solution{
 public:
    void createList(ListNode *head){
        ListNode *cur_node = head;
        for (int i = 1; i < 10; i++){
            ListNode *next_node = new ListNode;
            next_node->val = i;
            next_node->next = NULL;
            cur_node->next = next_node;
            cur_node = next_node;
        }
        cout << "create list successfully!" << endl;
    }

    void printList(ListNode *head){
        ListNode *cur_node = head;
        while (cur_node != NULL){
            cout << cur_node->val << "->";
            cur_node = cur_node->next;
        }
        cout << endl;
    }
};

int main(){
    Solution s;
    ListNode *head = new ListNode;
    head->val = 0;
    head->next = NULL;
    s.createList(head);
    s.printList(head);
    return 0;
}