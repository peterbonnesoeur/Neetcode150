class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        table = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8": 8,
            "9":9
        }

        num1_int, num2_int = 0,0
        for i in range(len(num1)):
            num1_int += table[num1[::-1][i]] * 10**i
        for i in range(len(num2)):
            num2_int += table[num2[::-1][i]] * 10**i

        return str(num1_int*num2_int)


class SolutionLeetcode:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10

        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str, res[beg:])
        return "".join(res)
