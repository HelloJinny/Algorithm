input_data = input().split(' ')

N = int(input_data[0])
X = int(input_data[1])

A = list(map(int, input().split(' ')))

# 1 5 3 4
for i in A:
    if X > i:
        print(i)