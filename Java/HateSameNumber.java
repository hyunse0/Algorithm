import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class HateSameNumber {
    public Integer[] solution(int[] arr) {
        return IntStream.concat(IntStream.of(arr[0]),
                        IntStream.range(1, arr.length)
                                .filter(i -> arr[i] != arr[i - 1])
                                .map(i -> arr[i]))
                .boxed()
                .toArray(Integer[]::new);
    }

    public static void main(String[] args) {
        HateSameNumber s = new HateSameNumber();
        System.out.println(s.solution(new int[]{1,1,3,3,0,1,1}));
    }
}
