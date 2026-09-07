# Last updated: 9/8/2026, 12:39:00 AM
1class MinStack:
2
3    def __init__(self):
4        self.stack = []
5        self.minStack = []
6
7    def push(self, value: int) -> None:
8        self.stack.append(value)
9
10        if not self.minStack:
11            self.minStack.append(value)
12        else:
13            self.minStack.append(min(value, self.minStack[-1]))
14
15    def pop(self) -> None:
16        self.stack.pop()
17        self.minStack.pop()
18
19    def top(self) -> int:
20        return self.stack[-1]
21
22    def getMin(self) -> int:
23        return self.minStack[-1]
24
25
26# Your MinStack object will be instantiated and called as such:
27# obj = MinStack()
28# obj.push(value)
29# obj.pop()
30# param_3 = obj.top()
31# param_4 = obj.getMin()