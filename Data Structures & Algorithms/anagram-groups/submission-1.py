class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        found_map = {}

        for i in strs:
            key = "".join(sorted(i))

            if key not in found_map:
                found_map[key] = []
       
            found_map[key].append(i)

        
        sorted_arr = list(found_map.values())

        return sorted_arr

        return [[""]]