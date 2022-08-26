#include <bits/stdc++.h>

using namespace std;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

struct ListNode{
    int val;
    ListNode *next;
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode dummy;
        ListNode* tail=&dummy;
        while(l1 && l2) {
            if(l1->val < l2->val) {
                tail->next=l1;
                l1=l1->next;
            }else{
                tail->next=l2;
                l2=l2->next;
            }
            tail=tail->next;
        }
        
        if(l1) tail->next = l1;
        if(l2) tail->next = l2;
        
        return dummy.next;
        
    }
};

int main(){

    vector<int> list1 = {1,7,9};
    vector<int> list2 = {1,2,4};
    Solution s;

    ListNode *head1 = new ListNode();
    head1 -> val = 1;
    head1 -> next = NULL;
    ListNode *current1 = head1;
    for(int i=1; i<list1.size() ; i++){
        current1 -> next = new ListNode();
        current1 = current1 -> next;
        current1 -> val = list1[i];
        current1 -> next = NULL;
    }
    printf( "data of list1: " );
    current1 = head1; 
    while(true){
        printf("%d", current1 -> val);
        current1 = current1 -> next;
        if (current1==NULL){
            break;
        }
    }
    printf("\n");

    ListNode *head2 = new ListNode();
    head2 -> val = 1;
    head2 -> next = NULL;
    ListNode *current2 = head2;
    for(int i=1; i<list2.size() ; i++){
        current2 -> next = new ListNode();
        current2 = current2 -> next;
        current2 -> val = list2[i];
        current2 -> next = NULL;
    }
    printf( "data of list2: " );
    current2 = head2; 
    while(true){
        printf("%d", current2 -> val);
        current2 = current2 -> next;
        if (current2==NULL){
            break;
        }
    }
    printf("\n");

    printf( "data of mergelist: " );
    ListNode *head3 = s.mergeTwoLists(head1,head2);
    while (true)
    {
        printf("%d", head3 -> val);
        head3 = head3 -> next;
        if (head3==NULL){
            break;
        }
    }
    

    return 0;
}