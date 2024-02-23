class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for c in s:
            if c in 'aeiouAEIOU':
                vowels.append(c)
        reversedVowels = vowels[::-1]
        newStr = ""
        i = 0
        for c in s:
            if c in 'aeiouAEIOU':
                newStr += reversedVowels[i]
                i += 1
            else:
                newStr += c
        return newStr

# Main
s = 'leEtcodE'
print(Solution().reverseVowels(s))