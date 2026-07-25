class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0

        result=0

        n = len(height)
        for i in range(n):
            print(i)
            #0203101321
            leftMax = rightMax = height[i]
            

            for j in range(i):
                leftMax = max(leftMax, height[j])

            for j in range(i + 1, n):
                rightMax = max(rightMax, height[j])

            
            result += min(leftMax, rightMax) - height[i]


        return result