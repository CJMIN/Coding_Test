


'''

< 볼링공 고르기 >

문제 :

A, B 두 사람이 볼링을 치고 있다.
두 사람은 서로 무게가 다른 볼링공을 고르려고 한다.
볼링공은 총 N개가 있으며 각 볼링공마다 무게가 적혀 있고 공의 번호는 1번부터 부여된다.
공의 무게가 같아도 부여된 번호가 다르면 다른공이다.
볼링공 무게는 1부터 M까지의 자연수 형태로 존재한다.

이때 두 사람이 볼링공을 고르는 경우의 수를 구하여라




입력 :
1 N, M [1|1000] [1|10]
2. 볼링공에 무게가 공백으로 구분되어 입력된다. 입력순서가 부여번호이다.




출력 :
경우의 수




아이디어 :
NC2 이므로 O(N^2)이다.
완전탐색으로 이중 반복문으로 구한 후 무게가 다른 경우에만 리스트에 넣고
리스트에 길이를 출력하자




설계 :
1. N , M 입력받기
2. 무게 리스트에 입력받기
3. 조합 리스트 만들기
4. 반복문 2개로 경우의 수 찾기
5. 무게가 다르면 조합리스트에 삽입하기



'''


import sys
import heapq
from collections import deque
import copy

input_sys=sys.stdin.readline

N,M=map(int,input().split())

weight_list=list(map(int,input_sys().rstrip().split()))

result_list=[]

for i in range(N):

    for j in range(i,N):

        if weight_list[i]!=weight_list[j]:

            result_list.append((i,j))


print(len(result_list))
