# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def Link_List(arr):
    head = ListNode(arr[0])
    curr = head
    for num in arr[1:]:
        curr.next = ListNode(num)
        curr = curr.next

    return head


class Solution:
    def sortList(self, head):
        def mergesort(head):
            if not head or not head.next:
                return head
            left = slow = fast = head
            fast = fast.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            right = slow.next
            slow.next = None

            sorted_left = mergesort(left)
            sorted_right = mergesort(right)
            return merge(sorted_left, sorted_right)

        def merge(l1, l2):
            dummy = ListNode(-1)
            prev = dummy
            while l1 and l2:
                if l1.val > l2.val:
                    prev.next = l2
                    l2 = l2.next
                else:
                    prev.next = l1
                    l1 = l1.next
                prev = prev.next
            prev.next = l1 or l2
            return dummy.next
        return mergesort(head)


if __name__ == "__main__":
    arr = [4, 2, 1, 3]
    ans = [1, 2, 3, 4]
    head = Link_List(arr)
    output = Solution().sortList(head)

    while output != None:
        print(output.val)
        output = output.next
