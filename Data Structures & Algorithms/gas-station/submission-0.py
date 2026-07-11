class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        n = len(gas)

        for i in range(n):
            tank = 0
            start = i
            end = n + (i - 1)
            flag = False
            for j in range(start, end+1):

                tank += gas[(j % n)]
                if tank - cost[(j%n)] < 0:
                    flag = True
                    break
                else:
                    tank = tank - cost[(j%n)]
            
            if not flag:
                return i
        
        return -1


        