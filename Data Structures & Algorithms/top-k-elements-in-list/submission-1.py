from collections import Counter
#^This makes a Counter func possible
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #brute force have a for loop that goes k elements  for nums 
        #extracts a number if the next one is equal and add one to number count
        #if not break, store the the value
        mp = Counter(nums)
        freqList=list(mp.items())
        freqList.sort(key=lambda x: x[1], reverse=True)
        
        kFreqList=[freqList[i][0] for i in range(k)]
        return kFreqList
           
