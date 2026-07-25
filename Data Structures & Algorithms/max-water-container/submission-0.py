class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        left = 0
        right = len(heights) - 1
        avg = 0

        while right > left:
            area = min(heights[left], heights[right]) * (right - left)
            avg = max(avg, area)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return avg