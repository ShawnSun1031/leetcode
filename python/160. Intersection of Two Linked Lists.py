# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        record = []
        lenA = 0
        headAA = headA
        while headA:
            lenA += 1
            record.append(headA.val)
            headA.val = -1
            headA = headA.next
        count = 0
        IsIntersect = False
        while headB:
            if headB.val == -1:
                IsIntersect = True
            if IsIntersect:
                count = count+1
            headB = headB.next
        
        if count == 0:
            for r in record:
                headAA.val = r
                headAA = headAA.next
            return None
        
        outputnode = lenA - count +1
        for r in record:
            headAA.val = r
            outputnode = outputnode - 1
            if outputnode == 0:
                output = headAA
            headAA = headAA.next
        return output

""" better solution 
共同的node: Common
listA = A + Common
listB =B + Common
PointerA: [A + Common + B] + Common
PointerB: [B + Common + A] + Common

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        while p1!=p2:
            if p1:
                p1 = p1.next
            else:
                p1 = headB
            if p2:
                p2 = p2.next
            else:
                p2 = headA
        return p2
"""