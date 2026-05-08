class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        sorted_freq = sorted(freq.items(), key = lambda x: x[1], reverse = True)
        print(freq)
        print(sorted_freq)
        frequent_items = []
        for key, val in sorted_freq:
            if k == 0:
                break
            frequent_items.append(key)
            k -= 1
        return frequent_items
            


        # 1 2 2 3 3 3
        # 0 - {}
        # 1 - {1}
        # 2 - {2}
        # 3 - {3}
        # 4 - {}
        # 5 - {}
        # 6 - {}
        