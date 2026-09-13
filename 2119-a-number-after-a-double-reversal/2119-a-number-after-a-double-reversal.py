class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        rev1 = self.reverse(num)
        rev2 = self.reverse(rev1)

        if rev2 == num:
            return True
        return False

    def reverse(self, num):
        arr = list(str(num))
        l = 0
        r = len(arr) - 1

        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

        return int("".join(arr))
