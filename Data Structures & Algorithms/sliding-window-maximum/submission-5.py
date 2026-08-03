class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        start = 0
        res = []

        for i in range(len(nums)):
            curr = nums[start:i + k]
            if len(curr) < k:
                return res
            curr.sort()
            res.append(curr[-1])
            start += 1


        return res