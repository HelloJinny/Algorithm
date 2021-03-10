input_data = input().split(' ')

H = int(input_data[0])
M = int(input_data[1])

M -= 45

if M < 0:
    M += 60
    H -= 1
    if H < 0:
        H = 23

print(str(H) + ' ' + str(M))