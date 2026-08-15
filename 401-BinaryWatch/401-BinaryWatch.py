# Last updated: 8/15/2026, 4:30:07 PM
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        leds = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]  # first 4 for hours, next 6 for minutes
        
        def backtrack(idx, count, hour, minute):
            if hour > 11 or minute > 59:
                return
            if count == turnedOn:
                res.append(f"{hour}:{minute:02d}")
                return
            for i in range(idx, 10):
                if i < 4:
                    backtrack(i + 1, count + 1, hour + leds[i], minute)
                else:
                    backtrack(i + 1, count + 1, hour, minute + leds[i])
        
        backtrack(0, 0, 0, 0)
        return res
