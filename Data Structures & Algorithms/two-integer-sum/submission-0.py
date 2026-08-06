class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map={}
        for i in range(len(nums)):
            target_i=target-nums[i]
            if target_i in num_map:
                return [num_map[target_i],i]
            num_map[nums[i]]=i
        return []
            