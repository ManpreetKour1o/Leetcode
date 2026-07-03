class Solution:
    def maxSubarraySumCircular(self, nums):
        total = sum(nums)

        current_max = max_sum = nums[0]
        current_min = min_sum = nums[0]

        for i in range(1, len(nums)):

            # Kadane for Maximum Subarray
            current_max = max(nums[i], current_max + nums[i])
            max_sum = max(max_sum, current_max)

            # Kadane for Minimum Subarray
            current_min = min(nums[i], current_min + nums[i])
            min_sum = min(min_sum, current_min)

        # If all numbers are negative
        if max_sum < 0:
            return max_sum

        # Maximum of normal and circular subarray
        return max(max_sum, total - min_sum)