class Solution(object):
    def findDuplicate(self, nums):
        seen = {}
        for i in nums: 
            if i in seen:
                return i
            seen[i] = seen.get(i,0)
        