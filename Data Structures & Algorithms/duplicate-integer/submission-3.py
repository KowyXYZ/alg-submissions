class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = []

        seen = set()

        for n in nums:
            if n not in duplicates: 
                duplicates.append(n)
            else :
                return True

        return False