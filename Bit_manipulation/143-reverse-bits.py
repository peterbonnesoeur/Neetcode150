# To redo
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = n >> i & 1
            print(bit, n>> i)
            res += bit << (31-i)
        return res

    def reverseBits_(self, n: int) -> int:
        num = str(bin(n))[2:]
        num = "0"*(32- len(num)) + num
        return int(num[::-1].encode('ascii'), base = 2)