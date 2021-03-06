# 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921

# 문제 설명
# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)

# 제한 조건
# n은 2이상 1000000이하의 자연수입니다.

# 하나씩 체크하는 방법(효율성 낮음)
# def isprime(n):
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True

# def solution(n):
#     answer = [isprime(i + 1) for i in range(n)]
#     return answer.count(True) - 1

def solution(n):
    num = set(range(2, n+1)) # {2,3,4,5,6,7,8,9,10}
    for i in range(2, n+1): # i = 2; i <= 10
        if i in num:
            num -= set(range(2*i, n+1, i)) # i의 배수의 집합을 생성한 뒤, num에서 제외
    return len(num) # 남은 배열의 원소 갯수 리턴

print(solution(10))

