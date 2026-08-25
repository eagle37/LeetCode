# Last updated: 8/25/2026, 11:02:22 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeKLists(self, lists):
8        
9        if not lists:
10            return None
11
12        def merge(l1, l2):
13            dummy = ListNode(0)
14            temp = dummy
15
16            while l1 and l2:
17                if l1.val < l2.val:
18                    temp.next = l1
19                    l1 = l1.next
20                else:
21                    temp.next = l2
22                    l2 = l2.next
23
24                temp = temp.next
25
26            temp.next = l1 if l1 else l2
27
28            return dummy.next
29
30        interval = 1
31
32        while interval < len(lists):
33            for i in range(0, len(lists) - interval, interval * 2):
34                lists[i] = merge(lists[i], lists[i + interval])
35
36            interval *= 2
37
38        return lists[0]