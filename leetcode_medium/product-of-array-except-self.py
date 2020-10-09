#https://leetcode.com/problems/product-of-array-except-self/
"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        i = 1
        j = length - 2
        z = 0
        
        fwd = {}
        back = {}
        final = []
        
        fwd[0] = nums[0]
        back[length - 1] = nums[length - 1]
        
        while i < length and j > -1 :
            fwd[i] = fwd[i-1] * nums[i]
            back[j] = back[j+1] * nums[j]
            i = i + 1
            j = j - 1
        
        z = 0
        while z < length:
            if(z-1 == -1):
                final.append(back[z+1])
            elif z + 1 == length:
                final.append(fwd[z-1])
            else:
                final.append(fwd[z-1] * back[z+1])
            z = z + 1

        return final
            
