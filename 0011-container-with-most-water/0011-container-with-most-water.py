class Solution:
    def maxArea(self, height: list[int]) -> int:
        n=len(height)
        right=n-1
        left=0
        maxarea=0
        while left<=right:
            h=min(height[left],height[right])
            w=right-left
            area=h*w
            maxarea=max(maxarea,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxarea