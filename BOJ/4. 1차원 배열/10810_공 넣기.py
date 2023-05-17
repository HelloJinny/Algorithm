# 첫째 줄에 N과 M이 주어진다.
N, M = map(int, input().split())

# 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다.
basket = [0 for i in range(N + 1)]

# 둘째 줄부터 M개의 줄에 걸쳐서 공을 넣는 방법이 주어진다.
for _ in range(M):
    # 각 방법은 세 정수 i j k로 이루어져 있다.
    i, j, k = map(int, input().split())
    for x in range(i, j + 1):
        basket[x - 1] = k

for x in range(N):
    print(basket[x], end=' ')