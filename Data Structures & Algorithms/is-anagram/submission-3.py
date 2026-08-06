class Solution:
    from collections import Counter  
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq={}
        t_freq={}
        for lett in s:
            s_freq[lett]=s_freq.get(lett,0)+1
        for lett in t:
            t_freq[lett]=t_freq.get(lett,0)+1
        return t_freq==s_freq