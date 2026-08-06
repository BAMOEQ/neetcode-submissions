class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for index,num in enumerate(nums): 
            num2=target-num
            if num2 in seen:
                return [seen[num2],index]
            seen[num]=index
    

