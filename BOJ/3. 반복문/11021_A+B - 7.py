import sys

T = int(input())

for i in range(T):
    input_data = sys.stdin.readline().rstrip().split(' ')
    A = int(input_data[0])
    B = int(input_data[1])
    print("Case #%s: %s" %(i+1, A + B))