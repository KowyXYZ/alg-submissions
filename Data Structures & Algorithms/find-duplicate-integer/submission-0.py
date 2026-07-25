class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        data = {}

        for num in nums:
            if num in data:
                data[num] += 1
            else:
                data[num] = 1
        
        mr = max(data, key=data.get)

        return mr