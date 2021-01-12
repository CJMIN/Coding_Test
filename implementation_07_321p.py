'''

럭키 스트레이트


문제 :
특정한 상황에서만 럭키 스트레이트를 사용할 수 있다.
현재 캐릭터의 점수를 N이라고 할 때 자릿수를 기준으로 점수 N을 반으로 나누어
왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 특정한 상황이라고 하자.



ex :

123402 -> 1+2+3 = 4+0+2 인 경우 럭키 스트레이트를 사용할 수 있다.

현재 점수 N이 주어지면 럭키 스트레이트를 사용할 수 있는 상태인지 알려주는 프로그램을 작성하라




입력 조건 :
1. N (항상 짝수의 자리수로 주어진다.)


출력 조건 :
특정한 상황이면 LUCKY

아니면 READY


아이디어 :
문자열의 길이를 세서 절반을 계산한 후에 비교하면 될 것 같다.


'''

import sys
import heapq
from collections import deque
import copy

input_sys=sys.stdin.readline


N=list(map(int,input_sys().rstrip().split()))

list_len=len(N)

first_num = 0
second_num = 0

for i in range(list_len//2):
    first_num+=i

for i in range(list_len//2,):
    second_num+=i


if first_num==second_num:
    print("LUCKY")
else:
    print("READY")

