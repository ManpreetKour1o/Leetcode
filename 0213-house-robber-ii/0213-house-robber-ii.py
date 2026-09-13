class Solution:
        def rob(self, nums: List[int]) -> int:
           if len(nums) == 1:
              return nums[0]

           return max(self.helper(nums[1:]), self.helper(nums[:-1]))

        def helper(self, nums):
            rob1 = 0
            rob2 = 0

            for n in nums:
               curr = max(rob2, rob1 + n)
               rob1 = rob2
               rob2 = curr

            return rob2