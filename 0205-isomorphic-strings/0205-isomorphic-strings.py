class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        S = {}
        T = {}

        for i in range(len(s)):
            a = s[i]
            b = t[i]

            if a in S and S[a] != b:
                return False

            if b in T and T[b] != a:
                return False

            S[a] = b
            T[b] = a

        return True

        