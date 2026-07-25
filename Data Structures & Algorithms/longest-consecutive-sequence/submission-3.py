class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums: return 0

        final_list = []

        num_set = set(nums)

        #num_set.discard(0)

        new_list = sorted(list(num_set))

        set_list = []

        if len(new_list) == 1:
            return 1

        
        
        for i in range(0, len(new_list), 1):
            set_list.append(new_list[i:i+2])


        filtered_list = []

        for i in set_list:
            if len(i) > 1:
                filtered_list.append(i)


        longest = 1

        for pair in filtered_list:
            if pair[1] == pair[0] + 1:
                final_list += [x for x in pair if x not in final_list]
                longest = max(longest, len(final_list))
            else:
                final_list = []
                

        return longest