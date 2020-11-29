//https://leetcode.com/problems/design-a-stack-with-increment-operation/submissions/

class CustomStack {
    List<Integer> stack;
    int max;
    public CustomStack(int maxSize) {
        stack = new ArrayList(maxSize);
        max = maxSize;
    }
    
    public void push(int x) {
        int current = stack.size();
        if(current< max){
            stack.add(x);
        }
        // System.out.println("push :"+stack);
    }
    
    public int pop() {
        int size = stack.size();
        // System.out.println("size :"+size);
        if(size > 0){
            Integer value = stack.get(size-1);
            stack.remove(size-1);
            // System.out.println("POP :"+stack);
            return value.intValue();
        }
        else{
            // System.out.println("POP :"+stack);
            return -1;
        }
        
    }
    
    public void increment(int k, int val) {
        int end = (k < stack.size()) ? k : stack.size();
        for(int i=0; i < end ; i++){
            stack.set(i, stack.get(i).intValue()+val);
        }
        // System.out.println("increment :"+stack);
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.push(x);
 * int param_2 = obj.pop();
 * obj.increment(k,val);
 */
