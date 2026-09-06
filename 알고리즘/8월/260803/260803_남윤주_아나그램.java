// 문자열의 문자들을 모두 사용해 재배열
// 부분문자열 중 문자의 구성이 동일한 것
// 주어진 문자열의 구성을 확인
// 긴 문자열에서 먼저 구성 같은 것을 찾아내고,
// 빠진 문자와 들어온 문자가 같은지 확인
// 아예 다른 문자가 들어왔다면 그 문자 다음 인덱스부터 확인
 
import java.util.*;
import java.io.*;
 
class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
 
        int T = Integer.parseInt(br.readLine());
 
        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
 
            String part = st.nextToken();
            String whole = st.nextToken();
 
            int partLength = part.length();
            int wholeLength = whole.length();
 
            int[] partCount = new int[26];
 
            for (int i = 0; i < partLength; i++) {
                partCount[part.charAt(i) - 'a']++;
            }
 
            int answer = 0;
            int start = 0;
 
            int[] windowCount = new int[26];
             
            // windowCount 리셋 필요성
            boolean needReset = true;
 
            while (start + partLength <= wholeLength) {
                if (needReset) {
                    windowCount = new int[26];
                    boolean canCheck = true;
                     
                    // 전체문자열에서 부분문자열 길이만큼 탐색
                    for (int i = start; i < start + partLength; i++) {
                        int index = whole.charAt(i) - 'a';
 
                        if (partCount[index] == 0) {
                            start = i + 1;
                            canCheck = false;
                            break;
                        }
 
                        windowCount[index]++;
                    }
 
                    if (!canCheck) {
                        needReset = true;
                        continue;
                    }
 
                    needReset = false;
                }
 
                if (isSame(partCount, windowCount)) {
                    answer++;
                }
 
                int outIndex = whole.charAt(start) - 'a';
                start++;
 
                if (start + partLength > wholeLength) {
                    break;
                }
 
                int inIndex = whole.charAt(start + partLength - 1) - 'a';
 
                windowCount[outIndex]--;
 
                if (partCount[inIndex] == 0) {
                    start = start + partLength;
                    needReset = true;
                    continue;
                }
 
                windowCount[inIndex]++;
            }
 
            sb.append("#").append(tc).append(" ").append(answer).append("\n");
        }
 
        System.out.print(sb);
    }
 
    static boolean isSame(int[] partCount, int[] windowCount) {
        for (int i = 0; i < 26; i++) {
            if (partCount[i] != windowCount[i]) {
                return false;
            }
        }
 
        return true;
    }
}
