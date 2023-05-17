# 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
students = [i for i in range(1, 31)]

for i in range(28):
    # 총 28줄로 각 제출자(학생)의 출석번호 n가 한 줄에 하나씩 주어진다.
    n = int(input())
    # 입력받은 숫자를 리스트에서 제거한다.
    students.remove(n)

# 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고,
print(min(students))

# 2번째 줄에선 그 다음 출석번호를 출력한다.
print(max(students))