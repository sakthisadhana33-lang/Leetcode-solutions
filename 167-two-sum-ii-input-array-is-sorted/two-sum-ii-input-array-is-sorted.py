class Solution(object):
    def twoSum(self, numbers, target):
        seen = {}
        n = len(numbers)
        for i in range(n):
            complement = target - numbers[i]
            if complement in seen:
                return [seen[complement], i+1]
            seen[numbers[i]] = i+1

        