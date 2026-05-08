class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ind = {}
        for i in range(len(strs)):
            sort_s = sorted(strs[i])
            sorted_s = "".join(sort_s)
            if sorted_s in ind:
                ind[sorted_s].append(i)
            else:
                ind[sorted_s] = [i]
            print(ind)
        anagrams = []
        for key, val in ind.items():
            ana = []
            for vals in val:
                ana.append(strs[vals])
            anagrams.append(ana)
        return anagrams

        