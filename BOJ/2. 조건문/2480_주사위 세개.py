A, B, C = map(int, input().split())

if A == B == C:
    reward = 10000 + A * 1000
    print(reward)
elif A == B or B == C:
    reward = 1000 + B * 100
    print(reward)
elif A == C:
    reward = 1000 + A * 100
    print(reward)
else:
    reward = max(A, B, C) * 100
    print(reward)