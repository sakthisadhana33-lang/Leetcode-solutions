class Solution(object):
    def groupAnagrams(self, strs):
        seen = {}
        for i in range(len(strs)):
            ch = tuple(sorted(strs[i]))
            if ch in seen:
                seen[ch].append(strs[i])
            else:
                seen[ch] = [strs[i]]
        return seen.values()