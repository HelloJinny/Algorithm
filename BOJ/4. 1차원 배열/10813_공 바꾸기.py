# 첫째 줄에 N과 M이 주어진다.
N, M = map(int, input().split())

# 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다.
basket = [i for i in range(1, N + 1)]

# 둘째 줄부터 M개의 줄에 걸쳐서 공을 교환할 방법이 주어진다.
for _ in range(M):
    # 각 방법은 두 정수 i j로 이루어져 있다.
    i, j = map(int, input().split())
    # i번 바구니와 j번 바구니에 들어있는 공을 교환한다.
    basket[i - 1], basket[j - 1] = basket[j - 1], basket[i - 1]

for x in range(N):
    print(basket[x], end=' ')