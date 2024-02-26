from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        prev_c = chars[0] if chars else ""
        count = 0
        for c in chars:
            if c == prev_c:
                count += 1
            else:
                if count == 1:
                    s += prev_c
                else:
                    s += prev_c
                    s += str(count)
                count = 1
            prev_c = c
        if count == 1:
            s += prev_c
        else:
            s += prev_c
            s += str(count)
        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)

# Main
chars = ["a", "a", "b", "b", "b"]
print(Solution().compress(chars))