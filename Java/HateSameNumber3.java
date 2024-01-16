import java.util.*;

public class HateSameNumber3 {
    public Stack<Integer> solution(int[] arr) {
        Stack<Integer> stack = new Stack<>();
        int before = -1;

        for (int now : arr) {
            if (now != before) {
                stack.push(now);
            }

            before = now;
        }

        return stack;
    }

}
