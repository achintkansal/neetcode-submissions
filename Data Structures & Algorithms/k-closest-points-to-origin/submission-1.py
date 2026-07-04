import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist = []
        for point in points:
            curr = []
            curr_dist = (point[0] ** 2 + point[1] ** 2) ** 0.5
            curr.append(curr_dist * -1)
            curr.append(point)

            print(curr)
            if len(dist) < k:
                heapq.heappush(dist, curr)
            
            elif (len(dist) == k) and (-1*dist[0][0]) > (-1*curr[0]):
                heapq.heappop(dist)
                heapq.heappush(dist, curr)
        res = []
        for d in dist:
            res.append(d[1])
        return res