class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, current, total):
            # Base case: target achieved
            if total == target:
                result.append(current[:])
                return

            # Base case: target exceeded
            if total > target:
                return

            # Try all candidates starting from 'start'
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                # Pass i (not i+1) because we can reuse the same element
                backtrack(i, current, total + candidates[i])
                current.pop()  # Backtrack

        backtrack(0, [], 0)
        return result
        