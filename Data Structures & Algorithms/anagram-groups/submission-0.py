class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #First I would make a Anagram hash map with keys that track all of the characters for anagrams
        anagramList={}
        for i in range(len(strs)):
            word=strs[i]
            key= "".join(sorted(word))

            if key in anagramList:
                anagramList[key].append(word)
            else:
                anagramList[key]=[word]
        return list(anagramList.values())
            
        #For each we want to check if the chars are in the hash map already else add it to the new list 