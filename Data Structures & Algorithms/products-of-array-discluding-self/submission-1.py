import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if nums == []:
            return []

        
        selector = 0
        final_array = []

        for i in range(len(nums)):
            if i == selector:
                
                filtered_list = nums[:selector] + nums[selector + 1:]

                final_array.append(math.prod(filtered_list))

                selector += 1

        

        return final_array

