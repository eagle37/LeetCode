# Last updated: 9/6/2026, 11:53:12 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l = []

        for i in tokens:
            if i.isalnum() or (i.startswith('-') and i[1:].isdigit()):
                l.append(int(i))
            else:
                x = l.pop()
                y = l.pop()

                if i == '+':
                    l.append(y + x)
                elif i == '-':
                    l.append(y - x)
                elif i == '*':
                    l.append(y * x)
                else:
                    l.append(int(y / x))

        return l[0]