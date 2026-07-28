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


    #c = p    exist = [p]          longest = 1
    # c = w    exist = [p, w]       longest = 2

    # c = w    duplicate!
    # remove p → [w]
    # remove w → []
    # add w    → [w]

    # c = k    exist = [w, k]       longest = 2
    # c = e    exist = [w, k, e]    longest = 3

    # c = w    duplicate!
    # remove w → [k, e]
    # add w    → [k, e, w]          longest = 3
