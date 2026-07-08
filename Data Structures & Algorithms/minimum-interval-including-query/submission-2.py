class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        resdict = {}
        res = []
        minheap = []

        sorted_queries = sorted(queries)
        intervals.sort(key = lambda i: i[0])

        q = 0
        i = 0

        while q < len(sorted_queries):
            #step1: push all intervals whose left <= q
            curr_query = sorted_queries[q]
            while i < len(intervals) and intervals[i][0] <= curr_query:
                len_interval = intervals[i][1] - intervals[i][0] + 1

                heapq.heappush(minheap, [len_interval, intervals[i][1]]) ## [len,right]
                i += 1
            
            # step2: remove all expired intervals
            while minheap and minheap[0][1] < curr_query: ## if right is less than query, it can never be the part of another subsequent queries, so remove it now
                heapq.heappop(minheap)
            
            ## output the min length from the minheap
            if minheap:
                resdict[curr_query] = minheap[0][0]
            else:
                resdict[curr_query] = -1
            
            q += 1

        print(resdict)
        for q in queries:
            res.append(resdict[q])


        
        return res



        