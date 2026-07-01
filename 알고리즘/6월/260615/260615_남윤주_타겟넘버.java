class Solution {
    int answer = 0;

    public int solution(int[] numbers, int target) {
        dfs(numbers, target, 0, 0);
        return answer;
    }

    private void dfs(int[] numbers, int target, int index, int sum) {
        //배열 마지막 원소까지 모두 탐색 완료 시 종료
        if (index == numbers.length) {
            if (sum == target) {
                answer++;
            }
            return;
        }

        dfs(numbers, target, index+1, sum + numbers[index]);
        dfs(numbers, target, index+1, sum - numbers[index]);
    }
}