https://leetcode.com/problems/max-consecutive-ones-iii/submissions/

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        i = 0
        maxLength = 0
        arrayLength = len(A)
    
        while ((arrayLength-i) > maxLength):
            j = i
            counter = 0
            length = 0
    
            while (j < arrayLength) and ((counter>=K and A[j]==1) or counter<K ):
                if A[j] == 0:
                    counter = counter +1
                    
                length = length +1
                j = j + 1
                
                if(arrayLength-j+length < maxLength): break
             
            if maxLength < length:
                maxLength = length
               
            i = i + 1
        return maxLength   
        
