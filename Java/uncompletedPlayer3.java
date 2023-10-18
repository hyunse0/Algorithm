import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
      String answer = "";
      HashMap<String, Integer> people = new HashMap<>();

      for (String p : participant) {
        people.put(p, people.getOrDefault(p, 0)+1);
      }

      for (String c : completion) {
        people.put(c, people.get(c)-1);
      }

      for (String p : participant) {
        if (people.get(p) != 0) {answer = p;}
      }

      return answer;
    }
}