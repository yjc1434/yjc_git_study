# 직사각형 별찍기
# https://programmers.co.kr/learn/courses/30/lessons/12969

# 문제 설명
# 이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
# 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

# 제한 조건
# n과 m은 각각 1000 이하인 자연수입니다.

# 반복문 이용
# a, b = map(int, input().strip().split(' '))
# line = ""
# for i in range(int(b)):
#     for j in range(int(a)):
#         line += "*"
#     line += "\n"
# print(line)

# 파이썬 문자열 곱하기
a, b = map(int, input().strip().split(' '))
line = ("*" * a + "\n") * b
print(line)