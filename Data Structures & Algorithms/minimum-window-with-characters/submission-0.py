from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        needed = Counter(t)
        window = {}

        required = len(needed)
        formed = 0

        left = 0

        best_length = float("inf")
        best_left = 0
        best_right = 0

        for right in range(len(s)):
            right_char = s[right]

            window[right_char] = window.get(right_char, 0) + 1

            if (
                right_char in needed
                and window[right_char] == needed[right_char]
            ):
                formed += 1

            while formed == required:
                current_length = right - left + 1

                if current_length < best_length:
                    best_length = current_length
                    best_left = left
                    best_right = right

                left_char = s[left]
                window[left_char] -= 1
                left += 1

                if (
                    left_char in needed
                    and window[left_char] < needed[left_char]
                ):
                    formed -= 1

        if best_length == float("inf"):
            return ""

        return s[best_left:best_right + 1]