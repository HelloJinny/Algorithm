# 현재 시각 A시 B분, 요리하는 데 필요한 시간 C
A, B = map(int, input().split())
C = int(input())

A += C // 60
B += C % 60

if B >= 60:
    B -= 60
    A += 1

if A >= 24:
    A -= 24

print(A, B)
