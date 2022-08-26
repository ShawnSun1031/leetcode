#include <bits\stdc++.h>

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
struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};


// class Solution {
// public:
//     ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
//         ListNode *head3 = new ListNode();
//         ListNode *curr3 = head3;
//         ListNode *pre3;
//         int temp,carry=0;
//         while(l1 != nullptr | l2 != nullptr){
//             temp = 0;
//             if (l1!=nullptr){
//                 temp += l1->val;
//             }else{
//                 temp += 0;
//             }
//             if (l2!=nullptr){
//                 temp += l2->val;
//             }else{
//                 temp += 0;
//             }
//             temp += carry;
 
//             if (temp/10!=0)
//             {
//                 carry = 1;
//                 curr3->val = temp%10;
//                 curr3->next = new ListNode();
//                 pre3 = curr3;
//                 curr3 = curr3->next;
                
//             }else{
//                 carry = 0;
//                 curr3->val = temp;
//                 curr3->next = new ListNode();
//                 pre3 = curr3;
//                 curr3 = curr3->next;
//             }
//             if(l1!=nullptr){
//                 l1 = l1->next;
//             }
//             if(l2!=nullptr){
//                 l2 = l2->next;
//             }
            
//         }
//         if (carry==1){
//             curr3->val = 1;
//         }else{
//             pre3->next = nullptr;
//         }
        

//         return head3;
        
//     }
// };

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        auto dummy = new ListNode();
        auto ptr = dummy;
        int c = 0;
        while(l1 or l2 or c){
            int sum = c;
            if(l1){
                sum += l1->val;
                l1 = l1->next;
            }
            if(l2){
                sum += l2->val;
                l2 = l2->next;
            }
            auto node = new ListNode(sum%10);
            c = sum/10;
            ptr->next = node;
            ptr = ptr->next;
        }
        return dummy->next;
    }
};

int main(){
    vector<int> list1 = {2,4,3};
    vector<int> list2 = {5,6,4};

    ListNode *head1 = new ListNode();
    ListNode *curr1 = head1;
    for (int i=0; i<list1.size(); ++i){
        curr1->val = list1[i];
        if (i==list1.size()-1){
            curr1->next = nullptr;
        }else{
            curr1-> next = new ListNode();
            curr1 = curr1-> next;
        }
    }

    ListNode *head2 = new ListNode();
    ListNode *curr2 = head2;
    for (int i=0; i<list2.size(); ++i){
        curr2 -> val = list2[i];
        if (i==list2.size()-1){
            curr2 ->next = nullptr;
        }else{
            curr2 -> next = new ListNode();
            curr2 = curr2 ->next;
        }
    }

    // while (head1!=nullptr)      
    // {
    //     cout << head1->val << endl;
    //     head1 = head1->next;
    // }
   

    // while (head2!=nullptr)      
    // {
    //     cout << head2->val << endl;
    //     head2 = head2->next;
    // }

    ListNode *head3 = new ListNode();
    head3 = Solution().addTwoNumbers(head1,head2);
    while (head3!=nullptr)      
    {
        cout << head3->val << endl;
        head3 = head3->next;
    }

    return 0;
}