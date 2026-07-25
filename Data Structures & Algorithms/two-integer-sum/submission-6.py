class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    

        for i in range(len(nums)):
            print(i)
            for j in range(1, len(nums)):
                print(j)
                if nums[i] + nums[j] == target and i is not j:
                    return [i, j]
    
        return [0,0]