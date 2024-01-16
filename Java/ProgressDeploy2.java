import java.util.*;

public class ProgressDeploy2 {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        int deployDay = (int) Math.ceil((double) (100 - progresses[0]) / speeds[0]);
        int cnt = 1;

        for (int i = 1; i < progresses.length; i++) {
            int newDay = (int) Math.ceil((double) (100 - progresses[i]) / speeds[i]);

            if (newDay > deployDay) {
                deployDay = newDay;
                answer.add(cnt);
                cnt = 1;
            } else {
                cnt++;
            }
        }

        answer.add(cnt);

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }

}
