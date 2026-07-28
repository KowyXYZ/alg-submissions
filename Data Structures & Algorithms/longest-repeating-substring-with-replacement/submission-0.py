class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0 

        for target in set(s):
            left = 0
            replacements = 0 

            for right in range(len(s)):
                if s[right] != target:
                    replacements += 1

                while replacements > k:
                    if s[left] != target:
                        replacements -= 1

                    left += 1
                
                lenght = right - left + 1
                longest = max(longest, lenght)

        return longest