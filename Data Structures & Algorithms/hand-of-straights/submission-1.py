class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False
        ### Its programming oriented problem
        total_hands = len(hand) // groupSize
        hm = {}
        hand.sort()

        for h in hand:
            if h not in hm:
                hm[h] = 1
            else:
                hm[h] += 1
        
        print(hm)
        for i in range(len(hand)):
            if hm[hand[i]] > 0:
                curr_element = hand[i]
                j = 0
                while j < groupSize:
                    # print(i, curr_element)
                    if (curr_element in hm) and (hm[curr_element] > 0):
                        hm[curr_element] -= 1
                    else:
                        # print(hm)
                        return False
                    curr_element += 1
                    j += 1
        return True
        
        