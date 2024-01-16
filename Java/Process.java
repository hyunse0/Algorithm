import java.util.*;

public class Process {
    public int solution(int[] priorities, int location) {
        int i = 0;
        int cnt = 0;
        int max = Arrays.stream(priorities).max().getAsInt();

        while (true) {
            if (priorities[i] == max) {
                priorities[i] = -1;
                cnt++;

                if (i == location) {return cnt;}
                max = Arrays.stream(priorities).max().getAsInt();
            }

            i++;
            if (i == priorities.length) {i = 0;}
            if (max == -1) {break;}
        }

        return cnt;
    }
}
