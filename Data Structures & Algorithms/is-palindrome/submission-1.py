class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_s = s.replace(" ", "")
        s_string = "".join(char.lower() for char in new_s if char.isalnum())



        if s_string == s_string[::-1]:
            print(s_string)
            print(s_string[::-1])
            return True
            

        return False