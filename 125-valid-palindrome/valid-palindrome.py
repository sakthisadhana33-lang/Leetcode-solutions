class Solution(object):
    def isPalindrome(self, s):
        l = []
        for i in s:
            if i.isalnum():
                l.append(i.lower())
        if l == l[::-1]:
            return True
        return False
        