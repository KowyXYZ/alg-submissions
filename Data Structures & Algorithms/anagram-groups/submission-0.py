class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        found_arr = {}

        for i in strs:
            key = "".join(sorted(i))
            if key not in found_arr:
                found_arr[key] = []
    
            found_arr[key].append(i)


        all_array = list(found_arr.values())

        return all_array


    


        return [[""]]