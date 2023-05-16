while True:
    input_data = input().split(' ')
    A = int(input_data[0])
    B = int(input_data[1])

    if A == 0 and B == 0:
        break

    print(A + B)