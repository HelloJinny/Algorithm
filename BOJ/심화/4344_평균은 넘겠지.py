# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
C = int(input())

# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다.
for _ in range(C):
    scores = list(map(int, input().split()))

    # 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
    avg = sum(scores[1:]) / scores[0]

    # 평균을 넘는 학생
    cnt = 0

    for i in scores[1:]:
        if avg < i:
            cnt += 1

    per = (cnt / scores[0]) * 100

    print('%.3f' % per + '%')
