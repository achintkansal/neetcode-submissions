class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, num in enumerate(temperatures):
            if not stack or num <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and num > temperatures[stack[-1]]:
                    prev_index = stack.pop()
                    res[prev_index] = (i - prev_index)
                stack.append(i)
        
        return res




        