# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        pre = head
        curr = head
        while curr!= None and curr!=True:
            curr = curr.next
            pre.next = True
            pre = curr
        if curr == None:
            return False
        else:
            return True

""" floyd cycle detection algo
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        #take a fast and slow pointer
        fast, slow = head, head
        #run while until the fast.next exists
        while fast and fast.next:
        
        #increment slow by 1 and fast by 2
            slow = slow.next
            fast = fast.next.next
            
            #if slow at any point catched up to fast. we know its not possible without a cycle in the list
            if( slow == fast ):
                return True
        # if while loop ends we return False
        return False
"""

if __name__ == "__main__":
    head_list = [3,2,0,-4]
    pos = 1

    head = ListNode(head_list[0])
    curr = head
    for idx,h in enumerate(head_list[1:], start=1):
        curr.next = ListNode(h)
        curr = curr.next
        if idx == pos:
            pos_node = curr
    curr.next = pos_node

    ans = Solution().hasCycle(head)
    print(ans)
