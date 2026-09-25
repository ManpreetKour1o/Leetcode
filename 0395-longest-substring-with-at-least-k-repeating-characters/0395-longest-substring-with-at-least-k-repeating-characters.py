class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in count:
            if count[ch] < k:
                left = self.longestSubstring(s.split(ch)[0], k)
                right = 0

                parts = s.split(ch)
                for part in parts[1:]:
                    right = max(right, self.longestSubstring(part, k))

                return max(left, right)

        return len(s)
        