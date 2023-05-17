# 첫째 줄에 정수의 개수 N이 주어진다.
N = int(input())

# 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다.
N_list = list(map(int, input().split()))

N_min = min(N_list)
N_max = max(N_list)

print('{} {}'.format(N_min, N_max))