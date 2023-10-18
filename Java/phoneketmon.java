import java.util.HashSet;
import java.util.Set;

class Solution {
    public int solution(int[] nums) {
      int maxCnt = (nums.length)/2;
      Set<Integer> set = new HashSet();
      
      for (int num : nums) {
        set.add(num);
      }

      int uniqueNumCnt = set.size();
      
      return (maxCnt < uniqueNumCnt) ? maxCnt : uniqueNumCnt;
    }
}