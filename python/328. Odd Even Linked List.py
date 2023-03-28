# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def Link_List(arr):
    head = ListNode(arr[0])
    curr = head
    for n in arr[1:]:
        curr.next = ListNode(n)
        curr = curr.next

    return head


class Solution:
    def oddEvenList(self, head):
        if head == None:
            return None
        if head.next == None:
            return head

        odd = head
        head_even = head.next
        even = head.next
        while odd != None or even != None:
            # print(even.val)
            if odd.next.next == None:
                break
            odd.next = odd.next.next
            odd = odd.next

            if even.next.next == None:
                break
            even.next = even.next.next
            even = even.next

        # if odd.next != None:
        #     odd.next = odd.next.next
        #     odd = odd.next
            # print(odd.val)
        if even.next != None:
            even.next = even.next.next
            even = even.next
        odd.next = head_even

        return head


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    # ans = [1, 3, 5, 2, 4]
    head = Link_List(arr)
    head = Solution().oddEvenList(head)
    while head != None:
        print(head.val)
        head = head.next
