# Last updated: 9/19/2026, 11:50:51 PM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10class Solution:
11    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':    
12        d = {None:None}
13        cur = head
14        
15        while cur:
16            d[cur] = Node(cur.val)
17            cur = cur.next
18            
19        cur = head
20        
21        while cur:
22            copy = d[cur]
23            copy.next = d[cur.next]
24            copy.random = d[cur.random]
25            cur = cur.next
26            
27        return d[head]