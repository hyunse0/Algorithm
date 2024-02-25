import java.util.PriorityQueue;

public class Spicy {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();

        for (int s : scoville) {
            heap.add(s);
        }

        int answer = 0;
        while (heap.size() >= 2 && heap.peek() < K) {
            int num1 = heap.poll();
            int num2 = heap.poll();

            heap.add(num1 + (num2*2));
            answer++;
        }

        if (heap.peek() < K) {
            answer = -1;
        }

        return answer;
    }
}
