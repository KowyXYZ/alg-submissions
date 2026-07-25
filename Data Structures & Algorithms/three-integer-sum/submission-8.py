class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()


        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            

            left = i + 1
            right = len(nums) - 1

            while right > left:
                total = nums[right] + nums[left] + nums[i]

                if total == 0:
                    result.append([nums[right], nums[left], nums[i]]) 

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif total > 0:
                    right -=1
            
                else:
                    left += 1
        
        return result
        # print(nums)

        # returnment = []

        # left = 0
        # right = len(nums) - 1 

        # while right > left:
        #     for i in range(len(nums)):
        #         if left != i and right != i:
        #          if (nums[left] + nums[right] + nums[i]) == 0:
        #             if (nums[left] == 0 and nums[right] == 0 and nums[i] == 0):
        #                 return [[0,0,0]]
        #             returnment.append([nums[left], nums[right], nums[i]])
                 
        #     left +=1
        #     right -=1
            

        # final_returnment = [list(x) for x in set(tuple(sorted(x)) for x in returnment)]

        # # if len(final_returnment) == 1:
        # #     degrouped = final_returnment[0]
        # #     for i in range(len(degrouped)):
        # #         if (degrouped[0] + degrouped[1] + degrouped[2]) == 0:
        # #             return []
                
               

        # return final_returnment
       

        # return []