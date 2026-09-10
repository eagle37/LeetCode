# Last updated: 9/10/2026, 10:23:05 PM
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        sign = 1

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)

            elif c in "+-":
                result += sign * num
                num = 0
                sign = 1 if c == "+" else -1

            elif c == "(":
                stack.append(result)
                stack.append(sign)

                result = 0
                sign = 1

            elif c == ")":
                result += sign * num
                num = 0

                sign = stack.pop()
                prev_result = stack.pop()

                result = prev_result + sign * result

        return result + sign * num