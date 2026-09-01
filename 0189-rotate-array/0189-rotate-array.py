class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def fun(l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        k=k%len(nums)
        fun(0,len(nums)-1)
        fun(0,k-1)
        fun(k,len(nums)-1)
        