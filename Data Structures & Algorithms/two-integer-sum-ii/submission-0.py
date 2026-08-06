class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for index,num in enumerate(numbers):
            target_num=target-num
            if target_num in seen:
                return [seen[target_num]+1,index+1]
            seen[num]=index
        