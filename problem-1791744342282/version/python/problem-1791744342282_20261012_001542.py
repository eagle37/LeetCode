# Last updated: 10/12/2026, 12:15:42 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
8        temp = l1
9        ans1 = 0
10        while temp:
11            ans1 = (ans1 * 10) + temp.val
12            temp = temp.next
13        temp1 = l2
14        ans2 = 0
15        while temp1:
16            ans2 = (ans2 * 10) + temp1.val
17            temp1 = temp1.next
18        ans = ans1 + ans2
19        ans = str(ans)
20        l3 = ListNode(val=int(ans[0]))
21        temp = l3
22        for i in range(1, len(ans)):
23            x = ListNode(val=int(ans[i]))
24            temp.next = x
25            temp = temp.next
26        return l3