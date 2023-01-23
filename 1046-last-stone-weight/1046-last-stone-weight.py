class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-1*ele for ele in stones]
        heapify(h)
        
        while len(h) >= 0:
            if len(h) > 1:
                max1 = -1*heappop(h)
                max2 = -1*heappop(h)
                if max1 != max2:
                    heappush(h, -1*(max1-max2))
            elif len(h) == 1:
                return -1*heappop(h)
            elif len(h) == 0:
                return 0
                            
        
        
        