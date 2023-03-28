# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def Link_List(arr):

    h = ListNode(1)
    temp = h
    for v in arr[1:]:
        h.next = ListNode(v)
        h = h.next
    h = temp

    return h


# class Solution:
#     def isPalindrome(self, head: ListNode):
#         forward = []
#         temp = head
#         while temp != None:
#             forward.append(temp.val)
#             temp = temp.next
#         for idx in range(len(forward)//2):
#             if forward[-(idx+1)] == head.val:
#                 head = head.next
#                 continue
#             else:
#                 return False
#         return True

# Floyd's Cycle Detection Algorithm
# time : O(n)
# space : O(1)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val:
                return False
            fast, slow = fast.next, slow.next
        return True


if __name__ == "__main__":
    head = [1, 2, 2, 1]
    ans = True
    h = Link_List(head)
    output = Solution().isPalindrome(h)
    print(output)
