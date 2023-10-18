import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    // 효율성 빵점~
    public String solution(String[] participant, String[] completion) {
        List<String> participantList = new ArrayList<>(Arrays.asList(participant));

        for (String c : completion) {
          participantList.remove(c);
        }
        
        return participantList.get(0);
    }
}