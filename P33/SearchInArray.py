class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        ans = -1
        while start <= end:
            mid = start + (end - start) // 2
            if target == nums[mid]:
                return mid
            # left side is sorted
            if nums[start] <= nums[mid]:
                # can ans be found in left side?
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            # right side is sorted
            else:
                # can ans be found in right side?
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return ans
