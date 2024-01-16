import java.util.*;

public class ProgressDeploy {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> queue = new LinkedList<Integer>();

        for (int i = 0; i < progresses.length; i++) {
            int deployDays = (int) Math.ceil((double) (100 - progresses[i]) / speeds[i]);
            queue.add(deployDays);
        }

        List<Integer> answer = new ArrayList<>();
        int today = 0;
        while (! queue.isEmpty()) {
            today = queue.remove();
            int cnt = 1;

            while (queue.peek() != null && today >= queue.peek()) {
                cnt++;
                today = Math.max(queue.remove(), today);
            }
            answer.add(cnt);
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }

}
