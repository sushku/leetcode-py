class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        base = str1 if len(str1) < len(str2) else str2
        gcd = ""
        while len(base) > 0:
            if len(str1) % len(base) == 0 and len(str2) % len(base) == 0:
                if base * (len(str1) // len(base)) == str1 and base * (len(str2) // len(base)) == str2:
                    gcd = base
                    break
            base = base[:-1]
        return gcd

# Main
str1 = "ABABABAB"
str2 = "ABAB"
print(Solution().gcdOfStrings(str1, str2))