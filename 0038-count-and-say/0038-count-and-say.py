class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"

        for _ in range(n - 1):
            new = ""
            count = 1

            for i in range(1, len(result)):
                if result[i] == result[i - 1]:
                    count += 1
                else:
                    new += str(count) + result[i - 1]
                    count = 1

            # Add the last group
            new += str(count) + result[-1]
            result = new

        return result