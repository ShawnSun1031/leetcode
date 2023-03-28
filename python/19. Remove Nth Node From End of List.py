# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def Link_List(arr):
    head = ListNode(arr[0])
    temp = head
    for v in arr[1:]:
        temp.next = ListNode(v)
        temp = temp.next

    return head


def print_linklist(head):
    while head != None:
        print(head.val)
        head = head.next


# class Solution:
#     def removeNthFromEnd(self, head, n):
#         temp = head
#         length = 0
#         while temp != None:
#             temp = temp.next
#             length += 1

#         remove_idx = length - n
#         if remove_idx == 0:
#             return head.next

#         cnt = 1
#         temp = head
#         while temp != None:
#             if cnt == remove_idx:
#                 temp.next = temp.next.next
#             else:
#                 temp = temp.next
#             cnt += 1

#         return head

# Two pointer
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head


if __name__ == "__main__":
    arr = [1]
    n = 1
    head = Link_List(arr)
    output = Solution().removeNthFromEnd(head, n)
    print_linklist(output)
