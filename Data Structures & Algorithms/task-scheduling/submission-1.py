from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map = {}

        for i in range(len(tasks)):
            if tasks[i] in freq_map:
                freq_map[tasks[i]] += 1
            else:
                freq_map[tasks[i]] = 1
        
        max_heap = []

        for key, value in freq_map.items():
            heapq.heappush(max_heap, [-1*value, key])
        
        queue = deque()
        curr_proc_time = 0

        while (len(max_heap) > 0) or (len(queue) > 0):

            curr_proc_time += 1
            while (len(queue) > 0) and (queue[0][2] + 1) <= curr_proc_time:
                task, freq, _ = queue.popleft()
                heapq.heappush(max_heap, [-1*freq, task])

            if len(max_heap) > 0:
                freq, task = heapq.heappop(max_heap)
                freq = abs(freq)

                freq -= 1
                if freq > 0:
                    queue.append([task, freq, curr_proc_time + n])
            
        
        return curr_proc_time



            
