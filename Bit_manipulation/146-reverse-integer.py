class Solution:
    def reverse(self, x: int) -> int:

        mul = 1
        if x<0:
            mul = -1
            x = -x
        x_str = str(x)
        min_x = bin(x%10)
        # -2 for the 0b at the beginning of the bin format
        # print(3*len(x_str) +len(min_x)-2, min_x)

        if 3*len(x_str) +len(min_x)-2 >=32:
            return 0

        return mul*int(str(x)[::-1])
