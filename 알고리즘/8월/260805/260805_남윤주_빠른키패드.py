1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
T = int(input())
 
keypad = (2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9)
 
for tc in range(1, T+1):
    char_num, word_cnt = input().split()
    words = list(input().split())
 
    word_length = len(char_num)
    ans = 0
     
    for word in words:
        if len(word) != word_length:
            continue
             
        okay = True
         
        for idx in range(word_length):
            target = keypad[ord(word[idx]) - ord('a')]
 
            if target != int(char_num[idx]):
                okay = False
                break
 
        if okay:
            ans += 1
 
    print(f'#{tc} {ans}')