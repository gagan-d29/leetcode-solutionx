class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        from collections import defaultdict
        left=0
        ans=0
        count=defaultdict(int)
        for right in range(len(fruits)):
            count[fruits[right]]+=1
            while len(count)>2:
                count[fruits[left]]-=1
                if count[fruits[left]]==0:
                    del count[fruits[left]]
                left+=1
            ans=max(ans,right-left+1)
        return ans
        