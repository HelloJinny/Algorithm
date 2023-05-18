# 첫째 줄에 숫자의 개수 N이 주어진다.
N = int(input())

# 둘째 줄에 숫자 N개가 공백없이 주어진다.
num = list(map(int, input()))

# 입력으로 주어진 숫자 N개의 합을 출력한다.
print(sum(num))