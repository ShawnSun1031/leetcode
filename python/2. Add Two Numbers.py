# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        l3 = ListNode()
        head3 = l3
        while(True):
            carry = 0
            if(l1!=None):
                l3.val += l1.val
                carry += int(l3.val /10)
                l3.val = l3.val % 10
                l1 = l1.next
            if(l2!=None):
                l3.val += l2.val
                carry += int(l3.val / 10)
                l3.val = l3.val % 10
                l2 = l2.next
            if (l1==None and l2==None):
                break
            else:
                l3.next = ListNode()
                l3 = l3.next
                l3.val += carry

        if carry != 0:
            l3.next = ListNode()
            l3 = l3.next
            l3.val = carry
        return head3



if __name__ == "__main__":
    list1 = [9,9,9,9,9,9,9]
    list2 = [9,9,9,9]
    l1 = ListNode()
    l2 = ListNode()
    head1 = l1
    head2 = l2
    l1.val = list1[0]
    l2.val = list2[0]
    for i in list1[1:]:
        l1.next = ListNode()
        l1 = l1.next
        l1.val = i
    for i in list2[1:]:
        l2.next = ListNode()
        l2 = l2.next
        l2.val = i
    s = Solution().addTwoNumbers(head1,head2)
    while s!=None:
        print(s.val)
        s = s.next
    
