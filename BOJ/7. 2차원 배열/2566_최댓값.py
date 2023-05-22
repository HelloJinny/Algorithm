# 첫째 줄부터 아홉 번째 줄까지 한 줄에 아홉 개씩 수가 주어진다.
table = [list(map(int, input().split())) for _ in range(9)]

max_num = 0
max_row = 0
max_col = 0

for row in range(9):
    for col in range(9):
        if max_num <= table[row][col]:
            max_row = row + 1
            max_col = col + 1
            max_num = table[row][col]

# 첫째 줄에 최댓값을 출력하고,
print(max_num)
# 둘째 줄에 최댓값이 위치한 행 번호와 열 번호를 빈칸을 사이에 두고 차례로 출력한다.
print(max_row, max_col)