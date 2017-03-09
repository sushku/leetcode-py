class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for strng in strs[1:]:
            min_len = min(len(strng), len(prefix))
            prefix = prefix[:min_len]
            for i in range(min_len):
                if strng[i] != prefix[i]:
                    prefix = prefix[:i]
                    break
            if len(prefix) == 0:
                break
        return prefix

s = Solution()
print(s.longestCommonPrefix(["abc", "abcd", "abe"]))
