class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for index,value in enumerate(nums):
            targetNum=target-value
            if targetNum in seen:
                return [seen[targetNum],index]
            seen[value]=index