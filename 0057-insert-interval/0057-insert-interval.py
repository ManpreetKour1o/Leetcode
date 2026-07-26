class Solution:
    def insert(self, intervals, newInterval):
        result = []

        for interval in intervals:

            # Current interval comes before newInterval
            if interval[1] < newInterval[0]:
                result.append(interval)

            # Current interval comes after newInterval
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval

            # Overlapping intervals
            else:
                newInterval = [
                    min(interval[0], newInterval[0]),
                    max(interval[1], newInterval[1])
                ]

        result.append(newInterval)

        return result
        