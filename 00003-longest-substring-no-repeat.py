class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        maxLength = 0
        subStr = ""
        for chr in s:
            index = subStr.find(chr)
            if index >= 0:
                if length > maxLength:
                    maxLength = length
                subStr = subStr[index+1:] + chr
                length = len(subStr)  # reset length
            else:
                length += 1
                subStr += chr

        if length > maxLength:
            maxLength = length

        return maxLength

# Main
s = "dvdf"
print(Solution().lengthOfLongestSubstring(s))