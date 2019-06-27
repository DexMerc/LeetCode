class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s=='':
            return True
        temp = ''
        op = {'(':1,'{':2,'[':3}
        ed = {')':1,'}':2,']':3}
        i = 0
        while i<len(s):
            if s[i] in op:
                temp+=s[i]
            else:
                if temp=='':
                    return False
                if ed.get(s[i])!=op.get(temp[-1]):
                    return False
                temp = temp[:-1]
            i+=1
        if len(temp)!=0:
            return False
        return True