# 첫째 줄에는 영수증에 적힌 총 금액 X가 주어진다.
X = int(input())

# 둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N이 주어진다.
N = int(input())

sum = 0

# 이후 N개의 줄에는 각 물건의 가격 a와 개수 b가 공백을 사이에 두고 주어진다.
for i in range(N):
    a, b = map(int, input().split())
    sum += a * b

if sum == X:
    print("Yes")
else:
    print("No")
