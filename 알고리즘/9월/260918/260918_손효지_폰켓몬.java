import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        
        for (Integer num : nums) {
            hashMap.put(num, hashMap.getOrDefault(num, 0) + 1);
        }
        
        int target = nums.length / 2;
        
        if (hashMap.size() > target) {
            answer = target;
        }
        else {
            answer = hashMap.size();
        };
        
        
        return answer;
    }
}