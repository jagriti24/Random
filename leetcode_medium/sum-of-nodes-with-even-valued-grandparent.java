// https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

class Solution {
    
    Integer sum = 0;
    
    public int sumEvenGrandparent(TreeNode root) {
        evenParents(root);
        System.out.println(sum);
        return sum;
    }
    
    private void evenParents(TreeNode node){
        if(node != null){
            if((node.val%2) == 0){
            
                if(node.left != null){
                    if(node.left.left != null){
                        sum += node.left.left.val;
                    }
                    if(node.left.right != null){
                        sum += node.left.right.val;
                    }
                }
                if(node.right != null){
                    if(node.right.left != null){
                        sum += node.right.left.val;
                    }
                    if(node.right.right != null){
                        sum += node.right.right.val;
                    }
                }
            }
        evenParents(node.left);
        evenParents(node.right);
        }
    }
}
