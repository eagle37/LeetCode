# Last updated: 10/21/2026, 9:32:29 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        temp = l1
        ans1 = 0
        while temp:
            ans1 = ans1 * 10 + temp.val
            temp = temp.next

        temp1 = l2
        ans2 = 0
        while temp1:
            ans2 = ans2 * 10 + temp1.val
            temp1 = temp1.next

        ans = ans1 + ans2
        div = 1

        while div <= ans // 10:
            div *= 10

        l3 = ListNode()
        temp = l3

        while div:
            x = ans // div
            temp.next = ListNode(x)
            temp = temp.next
            ans %= div
            div //= 10

        return l3.next