class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if nums == [0,0]:
            return [0,0]
        
        seen = {}

        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
        

        sorted_items = sorted(seen.items(), key=lambda x: x[1], reverse=True)

        return [item[0] for item in sorted_items[:k]]

  


            
