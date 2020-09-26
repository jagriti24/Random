#https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

class Solution(object):
    def queryString(self, S, N):
        i = 1
        while i<= N:
            result = S.find('{0:b}'.format(i))
            if result == -1:
                return False
            i = i+1
        return True
        
        
