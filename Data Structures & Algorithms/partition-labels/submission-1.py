class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        last_index = {}
        for i in range(len(s)):
            last_index[s[i]] = i
        
        i = 0
        res = []
        print(last_index)
        while i < len(s):

            curr_max_index = last_index[s[i]]
            count = 1
            while (i < curr_max_index):
                i += 1
                curr_max_index = max(curr_max_index,last_index[s[i]])
                count += 1

            res.append(count)
            i += 1
        
        return res





        