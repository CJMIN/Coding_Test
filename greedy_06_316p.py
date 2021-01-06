


'''

< 무지의 먹방 라이브 >

회전판에 먹어야 할 N개의 음식이 있다.
각 음식에는 1부터 N까지 번호가 붙어있다.
각 음식을 섭취하는데 일정시간이 소요된다.
1. 1번음식부터 먹기 시작하며
회전판은 번호가 증가하는 순서대로 음식을 앞으로 가져다 놓는다.
2. 마지막 번호의 음식을 먹은 후 회전판에 의해 다시 1번 음식이 앞으로 온다.
3. 음식 1개를 1초동안 섭취한 후에 남은 음식은 그대로 두고 다음 음식을 섭취한다.
다음 음식이란 아직 남은 음식 중 다음으로 섭취해야할 가장 가까운 번호의 음식을 말한다.
4. 회전판이 다음 음식을 앞으로 가져오는데 걸리는 시간은 없다고 가정한다.

무지가 먹방을 시작한지 k초후에  장애로 방송이 잠시 중단되었다.
몇번 음식부터 섭취해야하는지 알고자한다.

음식을 모두 먹는데 필요한 시간이 담겨있는 배열과 k초가 매개변수로 입력되면
몇번음식부터 다시 먹어야하는지를 반환하는 함수를 만들어라라




아이디어 :
k//N과 k%N을 이용하자
우선 정렬한 후에 k//음식의수이 가장 작은 수 보다 작다면 k%음식의수 + 1을 반환한다.
크다면 가장 작은 것을 pop하고 가장 작은 것의 크기를 A라고 하면
k=k-A*N으로 초기화 시키고 나머지 것들도 모두 A씩 빼준다.
그리고 음식의 수를 N-1로 초기화시킨다.




설계:
1. 배열 , k 입력받기
2. 음식의 값고 음식의 순서를 합쳐서 리스트 형태로 리스트에 삽입한다.
3. 2에서 만든 리스트 정렬하기
4. k를 음식의 수로 나눈 몫 share과 나머지 rest를 따로 저장한다.
5. 몫+before와 가장 작은 수(min)와 비교한다 (before 초기값 = 0)
6. 몫+before가 더 크면 [남은시간-(min-before)*음식수] 하고 before를 min으로 초기화해주고 min을 pop한다.
7. 몫+before가 더 작으면 남은시간%음식수 +1을 반환한다.
8. 몫이 더 작아지거나 리스트의 길이가 0이 될때까지 반복한다.




'''





def solution(food_times,k):

    idx=1
    current_food_list = []
    for i in food_times:
        current_food_list.append([i,idx])
        idx+=1

    food_times.sort()
    current_food_list.sort()

    second = k
    before = 0

    while True:

        num_of_food = len(current_food_list)

        share = second // num_of_food
        rest = second % num_of_food

        min = current_food_list[0][0]

        # print(current_food_list)
        # print("before : ", before)
        # print("min : ", min)
        # print("share : ",share)
        # print("second : ",second)

        if share + before <= min:
            return current_food_list[rest][1]
        else :
            second -= (min-before) * num_of_food

            while min in food_times:
                food_times.pop(0)
                current_food_list.pop(0)
            before = min

            # for i in range(len(current_food_list)):
            #     current_food_list[i][0]-=min

        if len(current_food_list)==0 and rest<second:
            return -1

        # if second // num_of_food == 0:
        #     return current_food_list[rest][1]




value1=[3,1,2,5,5,5,5,5,5,5,5,5,7,8,8,9]
value2=10000



print(solution(value1,value2))
print("#",sum([3,1,2,5,5,5,5,5,5,5,5,5,7,8,8,9]))
























# def solution(food_times, k):
#
#     num_of_food = len(food_times)
#
#     food_times_2=[]
#     count=0
#
#     for i in food_times:
#         food_times_2.append([i,count])
#         count+=1
#
#     last=0
#     idx = 0
#     flag=True
#
#     while k != 0:
#
#         # print(food_times_2)
#         food_times_2[idx][0] -= 1
#         k -= 1
#
#         num_len=len(food_times_2)
#
#         if food_times_2[idx][0]==0:
#
#             food_times_2.pop(idx)
#
#         if len(food_times_2)==num_len:
#             idx += 1
#
#
#         if idx == len(food_times_2):
#             idx = 0
#
#         if len(food_times_2)==0:
#             flag = False
#             break
#
#
#     if flag:
#         answer = food_times_2[idx][1] + 1
#     else:
#         answer = 1
#     return answer
#
# print(solution([3,1,2],2000))