class Solution(object):
    def moveZeroes(self, nums):
        k = 0

        for num in nums:
            if num != 0:
                nums[k] = num
                k += 1

        for i in range(k, len(nums)):
            nums[i] = 0

        