class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        ret = -1
        if not haystack:
            return ret
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if i + len(needle) > len(haystack):
                    break
                found = True
                for j in range(1, len(needle)):
                    if needle[j] != haystack[i+j]:
                        found = False
                        break
                if found:
                    ret = i
                    break
        return ret

s = Solution()
print(s.strStr("bacder", "cde"))
