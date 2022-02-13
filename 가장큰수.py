# 프로그래머스 가장 큰 수
# 문제 분류 : 정렬

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))
