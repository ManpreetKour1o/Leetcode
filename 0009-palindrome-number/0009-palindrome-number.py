class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums=str(x)
        n=len(nums)
        i=0
        j=n-1
        while i<=j:
            if nums[i]!=nums[j]:
                return False
            i+=1
            j-=1
        return True


        

        