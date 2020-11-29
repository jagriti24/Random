//https://leetcode.com/problems/path-sum/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean hasPathSum(TreeNode root, int sum) {
        boolean left = false;
        boolean right = false;
        
        if(root == null){
            return false;
        }
        
        int currentSum = sum-root.val;
        if(currentSum==0 && root.left==null && root.right==null){
            return true;
        }
        
        if(root.left != null){
            left = hasPathSum(root.left,currentSum);
        }
        
        if(root.right != null){
            right = hasPathSum(root.right,currentSum);
        }
        return left || right;
        
    }
}
