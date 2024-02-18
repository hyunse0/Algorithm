import java.util.LinkedList;
import java.util.Queue;

public class Truck {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> queue = new LinkedList<Integer>();

        int answer = 0;
        int i = 0;
        int queueSum = 0;

        while (i < truck_weights.length) {
            answer++;

            if (queue.size() == bridge_length) {
                queueSum -= queue.remove();
            }

            if (queueSum + truck_weights[i] <= weight) {
                queueSum += truck_weights[i];
                queue.add(truck_weights[i]);
                i++;
            } else {
                queue.add(0);
            }
        }

        if (queueSum > 0) {
            answer += bridge_length;
        }

        return answer;
    }
}
