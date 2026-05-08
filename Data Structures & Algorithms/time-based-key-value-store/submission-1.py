class TimeMap:

    def __init__(self):
        self.dict_key = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        '''
        1) dictionary for key: string, value: array pair
        2) store the values in (time, value) pair
        3) to retrieve the item use binary search on the pair and return the left index
        '''
        if key not in self.dict_key:
            self.dict_key[key] = [(timestamp, value)]
        else:
            self.dict_key[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.dict_key:
            return ""
            
        val = self.dict_key[key]

        left = 0
        right = len(val) - 1

        while left <= right:
            mid = left + ((right - left) // 2)

            if val[mid][0] == timestamp:
                return val[mid][1]
            elif timestamp > val[mid][0]:
                left = mid + 1
            else:
                right = mid - 1
        
        if right >= 0 and right < len(val):
            return val[right][1]
        else:
            return ""















        
            
