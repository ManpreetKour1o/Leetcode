class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res=0
        l=0
        ans=1
        for r in range(len(nums)):
            ans*=nums[r]
            while l<=r and ans >=k:
                ans =ans //nums[l]
                l+=1
            res+= (r-l+1)
        
        return res
        