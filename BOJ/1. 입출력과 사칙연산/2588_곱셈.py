A = int(input())
B = int(input())

out3 = A * ((B % 100) % 10)
out4 = A * ((B % 100) // 10)
out5 = A * (B // 100)

result = A * B

print(out3, out4, out5, result, sep='\n')