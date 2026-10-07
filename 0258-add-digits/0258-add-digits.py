class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            lst = list(str(num))
            sum = 0

            for i in range(len(lst)):
                sum += int(lst[i])

            num = sum

        return num

        