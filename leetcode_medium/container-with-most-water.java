//https://leetcode.com/problems/container-with-most-water/submissions/

class Solution {
    public int maxArea(int[] height) {
        int i = 0;
        int j = height.length-1;
        int max=0, prev=0, current=0,next=0 ;
        
        while(i!=j){
            
            if(height[i]<height[j]){
                // System.out.println("if");
                current = height[i]*(j-i);
                // System.out.println(current);
                next = i+1;
                while(next <= j && height[i] > height[next]){
                    next = next+1;
                }
                i = next;
            }
            else{
                // System.out.println("else");
                current = (j-i)*height[j];
                // System.out.println(current);
                prev = j-1;
                while(prev >= i && height[j] > height[prev]){
                    // System.out.println("prev :"+prev);
                    prev = prev-1;
                }
                j = prev;
            }
            // System.out.println("i : "+i+", j : "+j);
            // System.out.println(current);
            
            if(current > max){
                max = current;
            }
        }
        return max;
    }
}
