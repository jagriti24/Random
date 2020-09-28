#https://leetcode.com/problems/majority-element/


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nByTwo = floor(len(nums)/2)
        hashMap = {}

        for var in nums:
            if(hashMap.has_key(var)):
                val = hashMap[var] + 1
                hashMap[var] = val
            else:
                hashMap[var] = 1
        
        keyMax = max(hashMap, key=hashMap.get)
        return keyMax        
        
        
