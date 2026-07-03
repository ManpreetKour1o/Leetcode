class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        nums.sort()
        res=[]
        for i in range(n):
            if i >0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=n-1
            while l < r:
                s = nums[l] +nums[r] +nums[i]
                if s < 0:
                    l+=1
                elif s>0:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res        