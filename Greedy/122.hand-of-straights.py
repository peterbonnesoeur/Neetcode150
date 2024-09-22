from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False

        counted_occurences = Counter(hand)
        counter_keys = set(counted_occurences.keys())

        current_key = min(counter_keys)
        for i in range(len(hand)):
            current_val = counted_occurences.get(current_key, 0)
            if current_val == 0:
                return False
            else:
                counted_occurences[current_key] = current_val - 1
                if current_val - 1 == 0:
                    counter_keys.remove(current_key)
                current_key+=1
            # count += 1
            if (i+1)%groupSize ==0 and i+1 != len(hand):
                current_key = min(counter_keys)

        return True




    def isNStraightHandBrute(self, hand: List[int], groupSize: int) -> bool:

        if len(hand)%groupSize != 0:
            return False
        if len(hand)!=0 and groupSize == 1:
            return True

        hand = sorted(hand)
        maxL, maxR = 0,0
        cumSum = 1
        L = 0
        previous_element = hand[0]
        current_array = []

        while len(hand)!=0:
            for R in range(1,len(hand)):
                if hand[L] == hand[R]:
                    current_array.append(hand[R])
                    continue
                elif hand[L] + 1 == hand[R]:
                    cumSum+=1
                    L = R
                else:
                    return False

                if cumSum == groupSize:
                    break

            if cumSum!=groupSize:
                return False

            hand = current_array + hand[R+1:]
            current_array = []
            cumSum = 1
            L = 0

        return True