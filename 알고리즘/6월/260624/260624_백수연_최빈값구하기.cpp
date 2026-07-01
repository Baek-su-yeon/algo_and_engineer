// 문제 1.
// 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.
// 제한사항이 0 < array의 길이 < 100, 0 < array의 원소 < 1000이어서 풀로 돌아도 됨
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> array) {
    int answer = 0;
    
    int counts[1001] = {0};
    
    for (int num : array) counts[num] += 1;
    
    int max_count = 0;
    bool duplicated = false;
    
    for (int i = 0; i < 1000; i++)
    {
        if (max_count < counts[i])
        {
            duplicated = false;
            max_count = counts[i];
            answer = i; 
        }
        else if (max_count == counts[i] && counts[i] != 0) duplicated = true;
    }
    
    if (duplicated) return -1;
    return answer;
}