class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shash=dict();
        thash=dict();
        if len(s) != len(t):
            return False
        for char in t:
            thash[char]=thash.get(char,0)+1
        for char in s:
            shash[char]=shash.get(char,0)+1
        return shash == thash