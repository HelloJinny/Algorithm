num_list = []

for i in range(10):
    # 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다.
    num = int(input())
    # 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다.
    num_list.append(num % 42)

num_list = set(num_list)

# 서로 다른 나머지가 몇 개 있는지 출력한다.
print(len(num_list))