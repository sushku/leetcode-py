class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:
            h = min(height[i], height[j])
            area = h * (j - i)
            max_area = max(area, max_area)
            while height[i] <= h and i < j:
                i += 1
            while height[j] <= h and i < j:
                j -= 1
        return max_area

s = Solution()
print(s.maxArea([1,2,4,5,3,2]))
