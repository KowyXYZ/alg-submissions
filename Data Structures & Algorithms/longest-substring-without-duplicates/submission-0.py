class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #the idea here is to start counting x,y,z and if we get to X break
        exist = []
        longest = 0 

        for c in s:
            print(c)
            if c in exist: 
                while c in exist:
                    exist.pop(0)
                

            exist.append(c)
            longest = max(longest, len(exist))
        return longest
