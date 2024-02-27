class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i = 0
        for c in t:
            if c == s[i]:
                i += 1
                if i >= len(s):
                    return True
        return False

# Main
s = "ab"
t = "a"
print(Solution().isSubsequence(s, t))