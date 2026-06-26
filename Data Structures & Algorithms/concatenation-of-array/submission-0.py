class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = []
        n = len(nums)
        for i in range(2*n):
            l.append(nums[i%n])
        return l



        