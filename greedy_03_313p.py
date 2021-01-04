


'''

< 문자열 뒤집기 >



문제 :

0과 1로만 이루어진 문자열 S가 있다.

이 문자열 S에 있는 숫자를 전부 같게 만들려고 한다.

이때 할 수 있는 행동은 문자열 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다.

문자열 S의 숫자를 모두 같게 하기위해 뒤집어야하는 최소 횟수를 출력하라




입력 :

1. 문자열 S [1 | 1,000,000]




출력 :

행동의 최소 횟수




아이디어 :

한번 뒤집기 연산을 한 후의 연속된 숫자가 가장 길어지는 수를 선택하는 행위를

문자열의 숫자가 모두 같아질 때까지 하면 될 것 같다.




설계 :

# 1. 문자열 리스트로 입력받기
# 2. 서로다른 숫자가 시작되는 인덱스 찾아서 change리스트에 삽입하기
# 3. change 리스트에서 연속한 두값을 빼서 각 개수를 sum_of_3_list에 넣기

# 4. sum_of_3_list의 원소를 바꿔서 연속되는 값을 더한 후
# max_list에 해당 인덱스와 더한 값의 인덱스들을 튜플 형태로 넣기
# 5. 더한 값의 인덱스에 해당하는 원소에 더한 최대값을 저장한다.
# 6. 나머지 더한 값들의 인덱스에 해당하는 값들은 pop해준다.
# 7. sum_of_list의 원소가 1개가 될때까지 반복한다.




피드백 :

문제에 대해 좀 더 고민했으면 아주 쉽게 풀 수 있었다

너무 성급하게 풀려고만 하지 말고 생각하는데 시간을 좀 할애하자

그리디를 이용해서 짠 코드는 주석처리해놓았다.

'''


# 내가 짠 코드 :

# 1. 문자열 리스트로 입력받기
import sys
input_sys=sys.stdin.readline
from collections import deque
import heapq
import copy

s = list(map(int,input_sys().rstrip()))



# 2. 서로다른 숫자가 시작되는 인덱스 찾아서 change리스트에 삽입하기
change_idx=[]
first=s[0]
sum_of_3_list=[]



# 3. change 리스트에서 연속한 두 값을 빼서 각 개수를 sum_of_3_list에 넣기
idx=0
for i in s:
    if i != first:
        change_idx.append(idx)
        first=i
    idx+=1


count=(len(change_idx)+1)//2

print(count)


######################################################################################
######################################################################################
######################################################################################

if len(change_idx)==0:
    print("0")
    exit()

sum_of_3_list.append(change_idx[0])

for i in range(len(change_idx)-1):
    sum_of_3_list.append(change_idx[i+1]-change_idx[i])

sum_of_3_list.append(len(s)-change_idx[len(change_idx)-1])




count2=0

while True:

    max_list=[]

    # 4. sum_of_3_list의 원소를 바꿔서 연속되는 값을 더한 후
    # max_list에 해당 인덱스와 더한 값의 인덱스들을 튜플 형태로 넣기
    for i in range(len(sum_of_3_list)-1):

        if i==0:
            value=sum_of_3_list[i]+sum_of_3_list[i+1]
            max_list.append((value,i,i+1))
        else:
            value=sum_of_3_list[i-1]+sum_of_3_list[i] + sum_of_3_list[i + 1]
            max_list.append((value,i,i+1,i-1))

    max_list.sort(reverse=1)

    change_value=max_list[0]

    # 5. 더한 값의 인덱스에 해당하는 원소에 더한 최대값을 저장한다.
    sum_of_3_list[change_value[1]] = change_value[0]

    # 6. 나머지 더한 값들의 인덱스에 해당하는 값들은 pop해준다.
    idx_count=0
    for i in change_value:
        if idx_count>1:
            sum_of_3_list.pop(i)
        idx_count+=1
    count2+=1
    if len(sum_of_3_list)==1:
        break
    # 7. sum_of_list의 원소가 1개가 될때까지 반복한다.

print(count2)






























