class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_len = len(s)
        max_len = 0
        for k in range(str_len * 2 - 1):
            if k % 2 == 0:
                mid = k // 2
                i = mid - 1
                j = mid + 1
                pal_len = 1
            else:
                i = (k - 1) // 2
                j = (k + 1) // 2
                pal_len = 0
            while True:
                if i < 0 or j > (str_len - 1) or s[i] != s[j]:
                    if max_len <= pal_len:
                        max_len = pal_len
                        max_i = i + 1
                        max_j = j - 1
                    break
                pal_len += 2
                i -= 1
                j += 1

        return s[max_i:max_j + 1]

s = Solution()
print(s.longestPalindrome("babad"))
