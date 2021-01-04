#https://leetcode.com/problems/two-sum/


class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        for(int i=0 ; i < nums.length; i++){
           // if(nums[i]<= target){
               int diff = target-nums[i];
               // System.out.println("i: "+i);
               // System.out.println(diff);
               for(int j= i+1; j<nums.length; j++){
                   if(nums[j]==diff){
                       result[0] = i;
                       result[1] = j;
                       return result;
                   }
               // }
           } 
        }
        return result;
    }
}
