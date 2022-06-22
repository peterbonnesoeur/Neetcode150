#complicated exercise, need to make a deep note about it

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        A = nums1
        B = nums2

        if len(A) > len(B):
            B, A = A, B

        l, r = 0, len(A) - 1

        while True:

            i = (l + r) // 2
            j = half - i - 2 # -2 since both length needs to have
                             # -1 on them to start a proper indexing

            Aleft = A[i] if i>=0 else float('-infinity')
            Aright = A[i + 1] if i < len(A) - 1 else float('infinity')
            Bleft = B[j] if j >= 0 else float('-infinity')
            Bright = B[j + 1] if j < len(B) - 1 else float('infinity')

            if Aright >= Bleft and Bright >= Aleft:
                if total % 2:
                    return min(Aright, Bright)

                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2

            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1