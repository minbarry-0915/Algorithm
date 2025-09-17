import java.util.Deque;
import java.util.ArrayDeque;

class Solution {
    boolean solution(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        
        for (char ch: s.toCharArray()){
            if (ch == '('){
                stack.push(ch);
            } else if (ch == ')'){
                if (stack.isEmpty()){
                    return false;
                }
                stack.pop();
            }
        }
        
        return stack.isEmpty();
    }
}