class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        if len(s)-1 == 0:
            return True
        i = 0
        j = len(s)-1
        s=s.lower()
        while i < j:
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue
            if s[i]!=s[j]:
                return False
            else:
                i+=1
                j-=1
        return True