# 크로아티아 알파벳
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 첫째 줄에 최대 100글자의 단어가 주어진다.
word = input()

for i in croatia:
    word = word.replace(i, '*')

# 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
print(len(word))