class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        x = str(x)
        temp = ''
        if x[0]=='-':
            x=x[1:]
            temp+='-'
        if x[0]=='0':
            x=x[1:]
        for i in reversed(x):
            temp+=i
        temp = int(temp)
        if  abs(temp) >= (2**31)-1:
            return 0
        else:
            return int(temp)
        