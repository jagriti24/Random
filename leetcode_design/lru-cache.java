//https://leetcode.com/problems/lru-cache/

class LRUCache {
    Map<String, String> map;
    int maxLength;
    
    public LRUCache(int capacity) {
        map =  new LinkedHashMap<String, String>(capacity);
        maxLength = capacity;
    }
    
    public int get(int key) {
        String k = ""+key;
        if(map.containsKey(k)){
            String value = map.get(k);
            map.remove(k);
            map.put(k, ""+value);
            // System.out.println(map);
            // System.out.println(key+":"+value);
            return Integer.parseInt(value);
        }
        else{
            return -1;
        }
    }
    
    public void put(int key, int value) {
        String k = ""+ key;
        String v = ""+value;
    
        if(map.containsKey(k)){
            map.remove(k);
            map.put(k,v);  
        }
        else if(map.size() < maxLength){
            map.put(k,v);
            // System.out.println("if");
            // System.out.println(k+":"+v);
        }
        else{
            String first = map.entrySet().iterator().next().getKey();
            map.remove(first);
            map.put(k,v);
            // System.out.println("else");
            // System.out.println(k+":"+v);
        }
        // System.out.println(map);
        
    }
    
}
