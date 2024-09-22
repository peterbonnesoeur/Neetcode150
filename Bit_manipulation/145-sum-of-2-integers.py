
# To redo
class Solution:
    def getSum(self, a: int, b: int) -> int:

        def add(a,b):
            # print(not a, not b)
            # print("here")
            if not a or not b:
                return a or b
            return add(a^b,(a&b)<<1)

        if a*b < 0:
            if add(~a, 1) == b:
                return 0

            if a < 0:
                if add(~a, 1) > b:
                    # In case the positive of a is superior,
                    # it works as the binary expretion has enought
                    # bits
                    return add(a,b)
                else:
                    # otherwise, it fails, and so it is better
                    # to just invert the both of them and return
                    # the inverse
                    a_inv = add(~a,1)
                    b_inv = add(~b,1)
                    c = add(a_inv, b_inv)
                    return add(~c, 1)
            else:
                return self.getSum(b,a)

        return add(a,b)






        return add(a,b)