class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res=0
        sum=0
        count={0:1}
        for n in nums:
            sum+=n
            r=sum%k
            res+=count.get(r,0)
            count[r]=1+count.get(r,0)
        return res
        