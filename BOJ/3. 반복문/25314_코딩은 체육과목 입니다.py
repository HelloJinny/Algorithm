# 첫 번째 줄에는 문제의 정수 N이 주어진다.
N = int(input())

for _ in range(N // 4):
    print("long", end=" ")

print("int")

"""
long int: 4바이트
long long int: 8바이트
long long long int: 12바이트
long long long long int: 16바이트
"""