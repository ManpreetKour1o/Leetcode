class Solution:
    def firstUniqChar(self, s: str) -> int:
        a=list(s)
        freq={}
        for i in range(len(a)):
            freq[a[i]]=1+freq.get(a[i],0)
        for i in range(len(a)):
            if freq[a[i]]==1:
                return i
        return -1