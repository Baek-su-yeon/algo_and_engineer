import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] answers) {
        int[] one = {1, 2, 3, 4, 5};
        int[] two = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] three = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int s1 = 0, s2 = 0, s3 = 0;
        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == one[i % 5]) s1++;
            if (answers[i] == two[i % 8]) s2++;
            if (answers[i] == three[i % 10]) s3++;
        }
        
        int maxScore = Math.max(s1, Math.max(s2, s3));
        
        List<Integer> list = new ArrayList<>();
        if (maxScore == s1) list.add(1);
        if (maxScore == s2) list.add(2);
        if (maxScore == s3) list.add(3);
        
        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}