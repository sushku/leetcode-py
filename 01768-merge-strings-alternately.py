class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        res = ""
        while i < max(len(word1), len(word2)):
            if i < len(word1):
                res += word1[i]
            if i < len(word2):
                res += word2[i]
            i += 1
        return res

# Main
word1 = "ab"
word2 = "pqrs"
print(Solution().mergeAlternately(word1, word2))