//https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        int max = 0;
        Map<Character,Integer> countMap = new HashMap<Character,Integer>();
        
        // System.out.println(s.length());
        for(int i=0; i< s.length(); i++){
            countMap.put(s.charAt(i),1);
            for(int j = i+1; j<s.length(); j++){
                if(countMap.containsKey(s.charAt(j))){
                    // System.out.println("----------------");
                    // System.out.println(j);
                    if(countMap.size() > max){
                        max = countMap.size();
                    }
                    countMap.clear();
                    // System.out.println(max);
                    // System.out.println("----------------");
                    break;
                }
                else{
                    countMap.put(s.charAt(j),1);
                }
            }
            if(countMap.size() > max){
                    max = countMap.size();
            }
        }
        return max;
    }
}
