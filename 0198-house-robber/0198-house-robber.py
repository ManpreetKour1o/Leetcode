class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1=0
        rob2=0
        for n in nums:
            curr=max(rob2,rob1+n)
            rob1=rob2
            rob2=curr
        return rob2
        