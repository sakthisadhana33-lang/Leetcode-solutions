class Solution(object):
    def longestConsecutive(self, nums):
        num = set(nums)
        longest = 0
        count = 1
        for i in num:
            if i - 1 not in num:
                count = 1

                while i + count in num:
                    count += 1
            
            longest = max(longest, count)

        return longest            