class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])

# Main
s = " the sky   is   blue "
print(Solution().reverseWords(s))