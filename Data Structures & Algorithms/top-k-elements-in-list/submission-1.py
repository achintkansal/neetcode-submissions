class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = [[] for i in range(n+1)] ## bucket sort technique
        freq_dict = {}

        for num in nums:
            freq_dict[num] = 1 + freq_dict.get(num, 0)
        
        for key, val in freq_dict.items():
            print(key,val)
            freq[val].append(key)
        top_k = []
        for i in range(n, 0, -1):
            for vals in freq[i]:
                if len(top_k) == k:
                    break
                top_k.append(vals)
        
        return top_k
            





        # n = len(nums)
        # freq = {}
        # for num in nums:
        #     if num in freq:
        #         freq[num] += 1
        #     else:
        #         freq[num] = 1
        
        # sorted_freq = sorted(freq.items(), key = lambda x: x[1], reverse = True)
        # print(freq)
        # print(sorted_freq)
        # frequent_items = []
        # for key, val in sorted_freq:
        #     if k == 0:
        #         break
        #     frequent_items.append(key)
        #     k -= 1
        # return frequent_items
            


        # 1 2 2 3 3 3
        # 0 - {}
        # 1 - {1}
        # 2 - {2}
        # 3 - {3}
        # 4 - {}
        # 5 - {}
        # 6 - {}
        