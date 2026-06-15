#include <vector>
#include <iostream>
#include <deque>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    deque<int> answer_stack;
    
    // arr를 순회
    // 스택 top을 조회해서 같으면 pass, 비었거나 다르면 push
    // 이거 쓸거면 함수 출력 형식 vector<int> -> deque<int>로 바꿔야함
    for(int i = 0; i < arr.size(); i++)
    {
        int num = arr[i];
        if (answer_stack.empty() || num != answer_stack.back()) answer_stack.push_back(num);
    }
    
    // vector만 써야한다면
    for (int i = 0; i < arr.size(); i++)
    {
        int num = arr[i];
        if (answer.empty() || num != answer.back()) answer.push_back(num);
    }

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    // cout << answer << endl;

    return answer;
}