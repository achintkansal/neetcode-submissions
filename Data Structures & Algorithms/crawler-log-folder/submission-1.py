class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        inside = 0

        for log in logs:

            if log == '../':
                inside -= 1
                inside = max(0, inside)
            
            elif log == './':
                continue
            
            else:
                inside += 1
        
        return inside