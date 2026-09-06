#include <iostream>
#include <string>

using namespace std;
/*
문자열을 왼쪽부터 한 자리씩 확인

사전 순 앞 문자가 오면 원래 문자열 S보다 사전순으로 작아짐.

남은 문자들을 서로 다르게 배치하는 경우의 수 -> 팩토리얼 / 중복!

작은 문자들을 모두 확인한 뒤에는 실제 S의 현재 문자를 하나 사용한 것으로 처리하고 다음 자리로 넘어감.

이 과정 반복.

문자열 길이가 최대 20이라 long long 사용/
*/
long long fact[21];

long long calc(int cnt[26], int remain) {
    long long result = fact[remain];

    for (int i = 0; i < 26; i++) {
        result /= fact[cnt[i]];
    }

    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    fact[0] = 1;

    for (int i = 1; i <= 20; i++) {
        fact[i] = fact[i - 1] * i;
    }

    int tc, T;
    cin >> T;

    while (tc++ < T) {
        string S;
        cin >> S;

        int cnt[26] = {};

        for (int i = 0; i < S.size(); i++) {
            cnt[S[i] - 'A']++;
        }

        long long answer = 0;

        for (int i = 0; i < S.size(); i++) {
            int current = S[i] - 'A';

            for (int smaller = 0; smaller < current; smaller++) {

                if (cnt[smaller] == 0) {
                    continue;
                }
                cnt[smaller]--;

                int remain = S.size() - i - 1;

                answer += calc(cnt, remain);

                cnt[smaller]++;
            }

            cnt[current]--;
        }

        cout << "#" << tc << " " << answer << '\n';
    }

    return 0;
}