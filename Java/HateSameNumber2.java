import java.util.*;

public class HateSameNumber2 {
    public List<Integer> solution(int[] arr) {
        List<Integer> stack = new ArrayList<>();
        int before = -1;

        for (int now : arr) {
            if (now != before) {
                stack.add(now);
            }

            before = now;
        }

        return stack;
    }

}
