import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

public class clothes {
    public int solution(String[][] clothes) {
        Map<String, Integer> clothesMap = new HashMap<>();

        for (int i = 0; i < clothes.length; i++) {
            clothesMap.put(clothes[i][1], clothesMap.getOrDefault(clothes[i][1], 0)+1);
        }

        int answer = 1;
        for (Entry<String, Integer> entrySet : clothesMap.entrySet()) {
            answer *= entrySet.getValue()+1;
        }

        return answer-1; // 아무 것도 안입는 경우 제외
    }
}
