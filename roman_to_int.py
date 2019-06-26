class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dit = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        res = 0
        #for i in range(len(s)):
        i=0
        while i < len(s):
        	i+=1
            res += dit.get(s[i])
            if i>0:
                if dit.get(s[i])>last:
                    res -= 2*last
            last = dit.get(s[i])
        return res