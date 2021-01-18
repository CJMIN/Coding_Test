'''

뱀



문제 :

'Dummy' 라는 도스게임이 있다.
이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다.
뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다.
보드의 상하좌우 끝에 벽이 있다.
게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다.
뱀은 처음에 오른쪽을 향한다.

뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.

만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다.
즉, 몸길이는 변하지 않는다.

사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.





입력 :

첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100)
다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)

다음 K개의 줄에는 사과의 위치가 주어지는데,
첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다.
사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.

다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)

다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,
정수 X와 문자 C로 이루어져 있으며.
게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는
오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다.
X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.





출력 :

첫째 줄에 게임이 몇 초에 끝나는지 출력한다.




아이디어 :
모든 경우의 수가 작으므로 오나전탐색을 이용하여 풀 수 있다.
뱀이 존재하는 칸에는 -1로 초기화하고 테두리를 -1로 초기화하면 될 것 같다.

방향 회전 기능 구현
사과가 있는지 확인하는 기능 구현
뱀이 존재하는 칸 초기화하는 기능 구현(두가지 사과가 있는 경우 사과가 없는 경우)





입력 :
1. 보드의 크기 N 입력 받기
2. 사과 개수 K 입력 받기
3~+k-1. 사과의 위치 입력받기 -> 행 열 (모두 다르다)
3+k. 방향 변화 횟수 L 입력받기
3+k+1~. 시간 'L' 아니면 'D'

출력:
시간초


설계 :

# 입력받기
# 보드 판 구현하기 테두리는 -1 로 초기화 내부는 0으로 초기화하기
# 사과 위치 보드판에 1로 표시하기
# 뱀 꼬리 좌표를 저장하기 위한 변수 만들기

# 사과가 존재하는지 확인하는 기능 구현하기 (인풋 : 좌표) (아웃풋 : Bool 타입)
# 움직이는 함수 구현하기 (인풋 : 이전 좌표, 방향) (아웃풋 : 다음 좌표)
# 방향 변경하는 함수 구현하기 (인풋 : 방향문자,현재 방향 번호) (아웃풋: 변경된 방향 번호)
L이면 -1 R이면 +1
# 갈 수 있는 칸인지 확인하는 함수 구현하기 (인풋 : 좌표) (아웃풋 : Bool 타입)
# 뱀이 존재하는 칸 초기화하는 기능 구현하기 (인풋 : 사과여부, 뱀꼬리 좌표)

# count=0 , start =[1,1]
# 방향변수리스트 구현하기 [0,1,0,-1],[1,0,-1,0] 동남서북

# 다음 좌표로 움직이기
# -1 칸인지 확인하고 -1이면 시간 반환하고 끝 아니면 continue
# 시간 +1
# 방향 변경해야하면 방향 변경하기
# 사과 있는지 확인하기
# 사과 결과에 따라서 뱀이 존재하는 칸 초기화하기
# 무한 반복하기

피드백 :



'''


import sys
import heapq
from collections import deque
import copy
input_sys=sys.stdin.readline

N=int(input())
K=int(input())

board=[]
dir_r=[0,1,0,-1]
dir_c=[1,0,-1,0]

for i in range(N+2):
    temp=[-1 for _ in range(N+2)]
    board.append(temp)

for i in range(1,N+1):
    for j in range(1,N+1):
        board[i][j]=0

# for i in range(N+2):
#     print(board[i])

Apple=1
for i in range(K):

    row, col = map(int,input().split())

    board[row][col] = Apple



L=int(input())
dir_list=[]
for i in range(L):
    temp=list(input().split())
    idx_0=int(temp[0])
    temp[0]=idx_0
    dir_list.append(temp)


# for i in range(N+2):
#     print(board[i])

def check_apple(RC):
    # print(board[RC[0]][RC[1]])
    if board[RC[0]][RC[1]]==Apple:
        return True
    else:
        return False



def move_sneak(pre_rc,dir_num):

    next_dir=copy.deepcopy(pre_rc)

    next_dir[0]+=dir_r[dir_num]
    next_dir[1]+=dir_c[dir_num]


    return next_dir


def init_dir(dir_char,dir_num):

    if dir_char=='L':

        if dir_num==0:
            return 3 # idx problem
        else:
            return dir_num-1
    else:
        if dir_num==3:
            return 0 # idx problem
        else:
            return dir_num+1

def check_finish(rc):

    if board[rc[0]][rc[1]]==-1:
        return False
    else:
        return True

def init_board(appleOX,rc_tail):

    if appleOX==False:
        board[rc_tail[0]][rc_tail[1]]=0
        sneak_tail.popleft()

time_count=0
current_rc=[1,1]
dir_num=0
sneak_tail=deque([]) #start

while True:
    sneak_tail.append(current_rc)
    current_rc=move_sneak(current_rc,dir_num)
    time_count+=1

    flag=check_apple(current_rc)

    if not check_finish(current_rc):
        break
    else:
        board[current_rc[0]][current_rc[1]]=-1




    if len(dir_list)!=0 and dir_list[0][0]==time_count:
        dir_num=init_dir(dir_list[0][1],dir_num)
        dir_list.pop(0)

    # print(flag)
    init_board(flag,sneak_tail[0])

    # print("# time :",time_count)
    # print("# dir :",dir_list)
    # for i in range(N + 2):
    #     print(board[i])

print(time_count)










