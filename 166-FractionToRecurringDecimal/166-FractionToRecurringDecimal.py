# Last updated: 9/27/2026, 7:09:58 PM
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        if numerator == 0:
            return "0"

        sign = ""

        if (numerator < 0) != (denominator < 0):
            sign = "-"

        numerator = abs(numerator)
        denominator = abs(denominator)

        integer = numerator // denominator
        remainder = numerator % denominator

        if remainder == 0:
            return sign + str(integer)

        result = str(integer) + "."

        seen = {}

        while remainder != 0:

            if remainder in seen:
                pos = seen[remainder]
                result = result[:pos] + "(" + result[pos:] + ")"
                return sign + result

            seen[remainder] = len(result)

            remainder *= 10
            result += str(remainder // denominator)
            remainder %= denominator

        return sign + result