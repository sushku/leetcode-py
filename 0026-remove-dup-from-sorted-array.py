class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        prev = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != prev:
                nums[count] = nums[i]
                count += 1
                prev = nums[i]
        return count

s = Solution()
inp = [1, 1, 2]
count = s.removeDuplicates(inp)
print(inp[:count])
