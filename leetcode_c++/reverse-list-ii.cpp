/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *reverseBetween(ListNode *head, int m, int n) {
        ListNode *dummy = new ListNode(-1);
        dummy->next = head;
        ListNode *pre_m = dummy;
        ListNode *after_n = dummy;
        ListNode *node_m = head;
        ListNode *node_n = head;
        for (int i = 1; i < m; i++){
            pre_m = pre_m->next;
        }
        for (int i = 1; i < n; i++){
            node_n = node_n->next;
        }
        node_m = pre_m->next;
        after_n = node_n->next;
        node_n->next = NULL;
        pre_m->next = NULL; // 断开
        ListNode *pre = after_n;
        ListNode *cur = node_m;
        while (cur != nullptr){
            ListNode *next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }
        pre_m->next = pre;
        return dummy->next;
    }
};
