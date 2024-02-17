class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = s.split()
        print(lst)
        return ' '.join(lst[::-1])

s = Solution()
print(s.reverseWords("    the   sky   is blue"))
