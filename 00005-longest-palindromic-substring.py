class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenStr = len(s)
        root = s[0]
        pal = root
        maxPal = pal
        i = 0
        reachedEnd = False
        while i < lenStr:
            if lenStr == 1:
                break
            for j in range(1, lenStr):
                if len(root) == 1 and i-j >= 0 and i+j < lenStr and s[i-j] == s[i+j]:
                    pal = s[i-j] + pal + s[i+j]
                    if i+j == lenStr - 1:
                        reachedEnd = True
                        break
                elif len(root) == 2 and i-j >= 0 and i+1+j < lenStr and s[i-j] == s[i+1+j]:
                    pal = s[i-j] + pal + s[i+1+j]
                    if i+1+j == lenStr - 1:
                        reachedEnd = True
                        break
                else:
                    if len(pal) > len(maxPal):
                        maxPal = pal
                    if i+1 >= lenStr:
                        i += 1
                        break
                    if len(root) == 1 and s[i] == s[i+1]:
                        root = s[i] + s[i+1]
                    else:
                        root = s[i+1]
                        i += 1
                    pal = root
                    break
            if reachedEnd:
                if len(pal) > len(maxPal):
                    maxPal = pal
                break
        return maxPal

# Main
s = "babad"
print(Solution().longestPalindrome(s))