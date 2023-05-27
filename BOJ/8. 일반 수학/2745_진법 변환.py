# 첫째 줄에 N과 B가 주어진다.
N, B = input().split()
B = int(B)

# 첫째 줄에 B진법 수 N을 10진법으로 출력한다.
# int(a, b)는 문자열 a가 b에 해당하는 진수일때 정수로 바꿔준다.
print(int(N, B))