class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
          return False


        if s == '[]' or s == '()' or s == '{}':
            return True

        if "()[]{}" in s:
            return True


        matching = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        left = 0
        right = len(s) - 1

        print(s)
        while left < right:
            if s[left] not in matching:
                return False
            
            if matching[s[left]] != s[right]:
                return False

            left += 1
            right -= 1

        return True