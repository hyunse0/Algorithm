import java.util.Arrays;

class PhoneNumberList {
  public boolean solution(String[] phone_book) {
    // 문자 길이가 짧은 순으로 정렬
    Arrays.sort(phone_book, (String s1, String s2) -> s1.length() - s2.length());

    // 효율성 3, 4번 실패 => phone_book의 길이가 최대 1000000이므로 O(n^2)은 시간 초과..
    for (int i = 0; i < phone_book.length - 1; i++) {
      for (int j = i+1; j < phone_book.length; j++) {
        String s1 = phone_book[i];
        String s2 = phone_book[j];

        boolean allTheSame = true;
        for (int k = 0; k < s1.length(); k++) {
          if (s1.charAt(k) != s2.charAt(k)) {
            allTheSame = false;
            break;
          }
        }

        if (allTheSame) {return false;}
      }
    }

    return true;
  }

  public static void main(String[] args) {
    PhoneNumberList s = new PhoneNumberList();
    System.out.println(s.solution(new String[]{"123", "2345", "23467"}));
  }
}