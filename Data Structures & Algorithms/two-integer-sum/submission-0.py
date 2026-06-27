class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seendiff = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in seendiff.keys():
                if i != seendiff[nums[i]]:
                    return [seendiff[nums[i]],i]
            else:
                seendiff[diff]=i