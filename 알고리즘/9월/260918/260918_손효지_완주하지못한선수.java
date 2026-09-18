import java.util.HashMap;
import java.util.Map;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> hashMap = new HashMap<>() ;

        for (String part : participant) {
          hashMap.put(part, hashMap.getOrDefault(part, 0) + 1);
        }

        for (String comp : completion) {
          hashMap.put(comp, hashMap.get(comp) - 1);
        }

        for (Map.Entry<String, Integer> entry : hashMap.entrySet()) {
          if (entry.getValue() > 0) {
            answer = entry.getKey();
            break;
          }
        }
        return answer;
    }
}
