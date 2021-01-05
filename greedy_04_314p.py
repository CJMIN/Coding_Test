


'''

< 만들 수 없는 금액 >



문제 :

동네 편의점의 주인은 N개의 동전을 가지고 있다.
이때 N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하라.


입력 :
1. 동전의 개수 N [1 | 1000]
2. 화폐 단위를 나타내는 N개의 자연수가 공백으로 입력된다. 백만이하



출력 :
최솟값 출력



아이디어 :

최소값 최대값이면 그리디를 생각해야하므로
가장 작은 수 부터 만들 수 있는지 체크하면서 최소값을 찾으면 되겠다.
우선 입력받은 화폐의 단위를 정렬하고 하나씩 더해서 확인하자

주어진 코인들의 조합으로 만들 수 있는 가장 작은 조합들 만들어보자
NC1 + NC2 + NC3 + ... + NCN

시간복잡도 :

동전의 개수 1000이므로 NlogN을 생각하면 10000정도이다.
화폐의 단위 크기는 최소값을 구하는 것이기 때문에 시간 복잡도에 영향을 주지 않는다.



설계 :

1. 동전의 개수 입력받기
2. 화폐의 단위 리스트에 입력 받기
3. 정렬하기
4. 길이가 N인 체크리스트 생성하기
5.


'''

























