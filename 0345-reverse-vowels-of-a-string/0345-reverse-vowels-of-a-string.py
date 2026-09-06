class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=["a","e","i","o","u","A","E","O","I","U"]
        su=list(s)
        left=0
        right=len(su)-1
        while left<right:
            if su[left] not in vowels:
                left+=1
            elif su[right] not in vowels:
                right-=1
            else:
                su[left],su[right]=su[right],su[left]
                left+=1
                right-=1

        return"".join(su)
         
         
        