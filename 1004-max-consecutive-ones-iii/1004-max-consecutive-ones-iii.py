class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        zerocount=0
        left=0
        n=len(nums)
        for r in range(len(nums)):
            if nums[r]==0:
                zerocount+=1
            if zerocount>k:
                if nums[left]==0:
                    zerocount-=1
                left+=1
        return n-left