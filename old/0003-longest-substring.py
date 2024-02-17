class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        b = 0
        max_len = 0
        for e in range(len(s)):
            if s[e] in d and d[s[e]] >= b:
                # advance b
                b = d[s[e]] + 1
            # update dict
            d[s[e]] = e
            len_ = e - b + 1
            if len_ > max_len:
                max_len = len_
        return max_len

s = Solution()
print(s.lengthOfLongestSubstring("abba"))
