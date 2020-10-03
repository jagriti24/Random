#Ref : https://leetcode.com/problems/single-element-in-a-sorted-array/

"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
"""

import math

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        start = 0
        end = length-1
        midIndex = -1 
        
        if length%2 == 0:
            return 0
        
        if length == 1:
            return nums[0]
        
        
        while (end < length and start > -1):
            midIndex = start + int(math.ceil((end-start)/2))
            number = nums[midIndex]
            
            if start == end:
                return nums[start]
            
            if ((midIndex+1 < length) and (number != nums[midIndex+1])) and ((midIndex-1 > -1) and (number != nums[midIndex-1])):
                return number
            
            if midIndex%2 == 0:
                if (midIndex - 1) > -1 and (number == nums[midIndex-1]):
                    end = midIndex - 2
                elif (midIndex + 1) < length and (number == nums[midIndex+1]):
                    start = midIndex + 2
                    
            else:
                if (midIndex - 1) > -1 and (number == nums[midIndex-1]):
                    start = midIndex + 1
                elif (midIndex + 1) < length and (number == nums[midIndex+1]):
                    end = midIndex -1
        
                
            
          
        
