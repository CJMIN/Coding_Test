'''


문자열 재정렬

문제 :

알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다.

이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에 그 뒤에 모든 숫자를 더한 값을 이어서 출력하라.

ex :
KIKA5CB7이라는 값이 들어오면 ABCKK14을 출력한다.


입력 :
문자열 [1|10000]


출력 :



아이디어 :

sort를 이용하여 문자열을 오름차순으로 정렬한 후
문자열 중 숫자만 골라서 더한 후에 합친다.


설계 :
1. 입력받기
2. 정렬하기
3. 숫자 구별해서 더하기
4. 더한 숫자를 문자열 뒤에 붙이기


피드백 :

리스트에 있는 문자열을 합치는 함수인 join 숙지해둘 것

ord() 를 이용하면 문자열의 아스키코드를 구할 수 있다.

'''

import sys
import heapq
from collections import deque
import copy

input_sys=sys.stdin.readline

S = list(input())

S.sort()

sum=0
for i in range(10):
    while str(i) in S:

        sum+=i
        idx=S.index(str(i))
        S.pop(idx)

print("".join(S)+str(sum))
