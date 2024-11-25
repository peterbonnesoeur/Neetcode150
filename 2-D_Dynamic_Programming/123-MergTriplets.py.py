class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        good = set()
        for triplet in triplets:
            # Exclusion condition: If any of the values of the superposition element
            # is superior to the target, we will lose the element
            if (
                triplet[0] > target[0]
                or triplet[1] > target[1]
                or triplet[2] > target[2]
            ):
                continue
            for i in range(3):
                # Here, we just ensure that we have the right triplet added
                if triplet[i] == target[i]:
                    good.add(i)

        if len(good) == 3:
            return True
        else:
            return False
