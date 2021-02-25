n = int(input())
s = 0
i = 1

while True:
    s += i

    if n <= s:
        print(i)
        break

    i += 1