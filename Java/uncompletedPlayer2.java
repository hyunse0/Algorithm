import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
      String answer = "";
      HashMap<String, Integer> people = new HashMap<>();

      for (String p : participant) {
        if (people.get(p) == null) {
          people.put(p, 1);
        } else {
          people.put(p, people.get(p)+1);
        }
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