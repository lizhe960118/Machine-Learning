#include <stdlib.h>
#include <stdio.h>
#include <time.h>
//using namespace std;

//  * Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
 
class Solution {
public:
    ListNode *sortList(ListNode *head) {
        if (head == NULL || head->next == NULL){
            return head;
        }
        // 快慢指针找中心
        ListNode *fast, *slow;
        fast = head;
        slow = head;

        ListNode *mid;
        while(fast  && fast->next){
            fast = fast->next->next;
            slow = slow->next;
        }
        mid = slow->next;
        slow->next = NULL;

        ListNode *head1, *head2;
        head1 = sortList(head);
        head2 = sortList(mid);

        return sortTwoSortedList(head1, head2);
    }
    
private:
    ListNode *sortTwoSortedList(ListNode *head1, ListNode *head2){
        // if (head1 == NULL) return head2;
        // if (head2 == NULL) return head1;

        static ListNode dummy(0);

        ListNode *cur_pointer = &dummy;
        
        while (head1 && head2)
        {
            if (head1->val >= head2->val){
                cur_pointer->next = head2;
                head2 = head2->next;
            }
            else{
                cur_pointer->next = head1;
                head1 = head1->next;
            }
            cur_pointer = cur_pointer->next;
        }

        if (head1){
            cur_pointer->next = head1;
        }

        if (head2){
            cur_pointer->next = head2;
        }
        
        return dummy.next;
    }
};

void printList(ListNode *head){
    while (head != NULL)
    {
        printf("%d", head->val);
        head = head->next;
    }
    printf("\n"); 
}

ListNode* createList(int a[], int n){
    ListNode *head=NULL, *p = NULL;
    for (int i = 0; i < n; i++){
        if (head == NULL){
            head = p = new ListNode(a[i]);
        }else{
            p->next = new ListNode(a[i]);
            p = p->next;
        }
    }
    return head;
}

int main(int argc, char** argv){
    int n = 10;
    if (argc > 1){
        n = atoi(argv[1]);
    }
    srand(time(NULL));

    int *a = new int [n];
    for (int i = 0; i < n; i ++){
        a[i] = rand()%n + 1;
    }

    ListNode *head =  createList(a, n);
    printList(head);
    printList(Solution().sortList(head));

    system("pause");

    delete[] a;
    return 0;
}
