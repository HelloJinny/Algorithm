# 첫째 줄에 시험 본 과목의 개수 N이 주어진다.
N = int(input())

# 둘째 줄에 세준이의 현재 성적이 주어진다.
scores_list = list(map(int, input().split()))

# 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다.
M = max(scores_list)

# 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
for i in range(N):
    scores_list[i] = scores_list[i] / M * 100

# 첫째 줄에 새로운 평균을 출력한다.
print(sum(scores_list) / N)