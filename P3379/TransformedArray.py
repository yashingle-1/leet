class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            new_index = (i + nums[i]) % n
            res[i] = nums[new_index]

        return res