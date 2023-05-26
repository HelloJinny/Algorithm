rating = {"A+": 4.5, "A0": 4.0,
          "B+": 3.5, "B0": 3.0,
          "C+": 2.5, "C0": 2.0,
          "D+": 1.5, "D0": 1.0,
          "F": 0.0}

rate = 0
scoreSum = 0

for _ in range(20):
    # 20줄에 걸쳐 치훈이가 수강한 전공과목의 과목명, 학점, 등급이 공백으로 구분되어 주어진다.
    subject, score, grade = input().split()

    # P/F 과목의 경우 등급이 P또는 F로 표시되는데, 등급이 P인 과목은 계산에서 제외해야 한다.
    if grade == "P":
        continue

    rate += float(score) * rating[grade]
    scoreSum += float(score)

# 치훈이의 전공평점을 출력한다.
# 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.
print(rate / scoreSum)