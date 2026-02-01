class Solution(object):
    def minimumCost(self, nums):
        first = nums[0]
        mn1 = mn2 = float('inf')

        for x in nums[1:]:
            if x < mn1:
                mn2 = mn1
                mn1 = x
            elif x < mn2:
                mn2 = x

        return first + mn1 + mn2
