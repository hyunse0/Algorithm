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

  public static void main(String[] args) {
    Solution s = new Solution();
    System.out.println(s.solution(new int[]{3, 1, 2, 3}));
  }
}
  

