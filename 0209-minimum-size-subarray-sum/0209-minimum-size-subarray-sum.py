class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=float('inf')
        l=0
        ans=0
        for r in range(len(nums)):
            ans+= nums[r]
            while ans>=target:
                res=min(res,r-l+1)
                ans-=nums[l]
                l+=1
            
        return res if res < float('inf') else 0


        