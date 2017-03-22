class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        R = S.replace('-', '').upper()
        chars = len(R)
        grp1 = K if chars % K == 0 else chars % K
        new_str = R[:grp1]
        for start in range(grp1, chars, K):
            new_str += "-" + R[start:start+K]
        return new_str

s = Solution()
print(s.licenseKeyFormatting("2-4A0r7-4k", 3))
