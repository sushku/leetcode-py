class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        rev = sign * int(str(abs(x))[::-1])
        if abs(rev) >= 2 ** 31:
            return 0
        else:
            return rev

s = Solution()
print(s.reverse(-123))
