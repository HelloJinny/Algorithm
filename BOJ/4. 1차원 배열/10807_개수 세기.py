# 첫째 줄에 정수의 개수 N이 주어진다.
N = int(input())

# 둘째 줄에는 정수가 공백으로 구분되어져있다.
N_list = list(map(int, input().split()))

# 셋째 줄에는 찾으려고 하는 정수 v가 주어진다.
v = int(input())

# 첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.
print(N_list.count(v))