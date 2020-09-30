https://leetcode.com/problems/max-consecutive-ones-iii/submissions/

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        maxLength = 0
        hashTracker = {}
        i = 0
        countOfZero = 0
        hashTracker[countOfZero] = -1
        while i < len(A):
            if(A[i] == 0):
                countOfZero = countOfZero + 1
                hashTracker[countOfZero] = i
                
            startPos = countOfZero - K
            if startPos >= 0:
                length = i - hashTracker[startPos]
            else:
                length = i+1
            if(length > maxLength):
                    maxLength = length    
            i = i+ 1
        return maxLength
                    
                
        
 
