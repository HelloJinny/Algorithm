# 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
N, M = map(int, input().split())

# 각각의 바구니에는 1번부터 N번까지 번호가 순서대로 적혀져 있다.
# 바구니는 일렬로 놓여져 있고, 가장 왼쪽 바구니를 1번째 바구니, 그 다음 바구니를 2번째 바구니, ..., 가장 오른쪽 바구니를 N번째 바구니라고 부른다.
basket = [i for i in range(1, N + 1)]

# 둘째 줄부터 M개의 줄에는 바구니의 순서를 역순으로 만드는 방법이 주어진다.
for i in range(M):
    # 방법은 i j로 나타낸다.
    i, j = map(int, input().split())
    # 왼쪽으로부터 i번째 바구니부터 j번째 바구니의 순서를 역순으로 만든다는 뜻이다.
    basket[i - 1:j] = basket[i - 1:j][::-1]

for x in range(N):
    print(basket[x], end=' ')