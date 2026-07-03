class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        seen={}
        res=[]
        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]]+=1
            else:
                seen[nums[i]]=1
           
            if seen[nums[i]] > len(nums)//3 and nums[i] not in res:
                res.append(nums[i])
        return res
        