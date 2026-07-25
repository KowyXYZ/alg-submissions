class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_arr = {}
        t_arr = {}

        for i in s:
            if i in s_arr:
                s_arr[i] += 1
            else:
                s_arr[i] = 1

        for i in t:
            if i in t_arr:
                t_arr[i] += 1
            else:
                t_arr[i] = 1


        if len(s_arr) != len(t_arr):
            return False
                
        for s_key, s_value in s_arr.items():
            found = False

            for t_key, t_value in t_arr.items():
                if s_key == t_key and t_value == s_value:
                    found = True
                    break

        if not found:
            return False
        
       
        return True