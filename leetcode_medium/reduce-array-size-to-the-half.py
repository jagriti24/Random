#https://leetcode.com/problems/reduce-array-size-to-the-half/
"""
Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

 

Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.
Example 2:

Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.
Example 3:

Input: arr = [1,9]
Output: 1
Example 4:

Input: arr = [1000,1000,3,7]
Output: 1
Example 5:

Input: arr = [1,2,3,4,5,6,7,8,9,10]
Output: 5
 

Constraints:

1 <= arr.length <= 10^5
arr.length is even.
1 <= arr[i] <= 10^5
"""

class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        hash_map = {}
        min_len = len(arr)/2
        final = 0
        
        for a in arr:
            if hash_map.has_key(a):
                hash_map[a] += 1
            else:
                hash_map[a] = 1
                
        # print hash_map
        val = sorted(hash_map.values())
        # print val
        local_sum = 0
        for k in range(len(val)-1,-1,-1):
            # print "here"
            # print val[k]
            local_sum += val[k]
            final += 1
            if(local_sum >=min_len):
                break
            
            
        return final
                    
