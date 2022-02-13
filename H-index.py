# 프로그래머스 H-index
# 문제 분류 : 정렬

def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()
    for h in range(n+1):
        for i, c in enumerate(citations):
            if c >= h and n - i >= h:
                answer = max(answer, h)
    return answer
