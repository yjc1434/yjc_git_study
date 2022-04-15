# 약수의 합
# https://programmers.co.kr/learn/courses/30/lessons/12928

# 문제 설명
# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

# 제한 사항
# n은 0 이상 3000이하인 정수입니다.

def solution(n):
    answer = 0
    for i in range(n):
        if n % (i + 1) == 0:
            answer += (i + 1)
    return answer

print(solution(12))