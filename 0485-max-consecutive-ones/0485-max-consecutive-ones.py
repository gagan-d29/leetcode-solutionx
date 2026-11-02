class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        current_count = 0
        n = len(nums)
        max_count = 0
        for j in range(0, n):
            if nums[j] == 1:
                current_count += 1
            else:
                max_count = max(max_count, current_count)
                current_count = 0
        return max(max_count, current_count)
