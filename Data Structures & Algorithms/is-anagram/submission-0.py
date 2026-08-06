class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            s_hash={}
            t_hash={}
            for h in s:
                s_hash[h]= s_hash.get(h,0)+1
            for p in t:
                t_hash[p]=t_hash.get(p,0)+1
            return s_hash == t_hash