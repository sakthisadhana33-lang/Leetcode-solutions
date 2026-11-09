class Solution(object):
    def majorityElement(self, nums):
        count = 0
        candidate = None
        for i in nums:
            if count == 0:
                candidate = i
            if candidate == i:
                count += 1
            else:
                count -= 1
        return candidate        