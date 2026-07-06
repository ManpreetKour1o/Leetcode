class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)>len(s) or len(s)>len(t):
            return False
        pcount={}
        scount={}
        for i in range(len(s)):
            pcount[s[i]]=1+pcount.get(s[i],0)
            scount[t[i]]=1+scount.get(t[i],0)
        return True if scount==pcount else False
        