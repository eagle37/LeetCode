# Last updated: 10/12/2026, 12:19:25 AM
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
11            ans1 = ans1 * 10 + temp.val
12            temp = temp.next
13
14        temp1 = l2
15        ans2 = 0
16        while temp1:
17            ans2 = ans2 * 10 + temp1.val
18            temp1 = temp1.next
19
20        ans = ans1 + ans2
21        div = 1
22
23        while div <= ans // 10:
24            div *= 10
25
26        l3 = ListNode()
27        temp = l3
28
29        while div:
30            x = ans // div
31            temp.next = ListNode(x)
32            temp = temp.next
33            ans %= div
34            div //= 10
35
36        return l3.next