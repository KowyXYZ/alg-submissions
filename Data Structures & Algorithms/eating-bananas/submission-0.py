class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        final = r

        while l <= r:

            k = (l + r) // 2
            hours = 0

            for i in piles:
              hours += math.ceil(i / k)

            if hours <= h:
                final = min(final, k)
                r = k - 1
            else:
                l = k + 1

        return final    
               

       
        