num_list = []

for i in range(9):
    num_list.append(int(input()))

# 첫째 줄에 최댓값을 출력하고
print(max(num_list))

# 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.
print(num_list.index(max(num_list))+1)