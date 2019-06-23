#include<iostream>
using namespace std;

struct ListNode {
        int val;
        ListNode *next;
        ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        ListNode *dummy = new ListNode(-1);
        ListNode *cur = dummy;
        int flag = 0;
        int value = 0;
        while(l1 != nullptr || l2 != nullptr){
            if (l1 != nullptr && l2 != nullptr ){
                value = l1->val + l2->val + flag;
                l1 = l1->next;
                l2 = l2->next;
            } else if (l1 != nullptr){
                value = l1->val + flag;
                l1 = l1->next;
            } else {
                value = l2->val + flag;
                l2 = l2->next;
            }
            if (value >= 10){
                value = value - 10;
                flag = 1;
            } else {
                flag = 0;
            }
            ListNode *next_node = new ListNode(value);
            cur->next = next_node;
            cur = next_node;
        }
        if (flag != 0){
            ListNode *next_node = new ListNode(1);
            cur->next = next_node;
        }
        return dummy->next;
    }
};