import sys


def flip(n):  # 0 ~ n 범위의 팬케익을 뒤집는 함수
    if n != 0:
        tmp = []
        for i in range(n, -1, -1):
            tmp.append(cakes[i])
        cakes[0:n+1] = tmp

        answer[0] += 1
        answer.append(n+1)


T = int(input())
while T:
    cakes = []
    li = sys.stdin.readline().split()
    li = [int(x) for x in li]
    cakes = li[1:]
    answer = [0]
    # 어디까지 쌓였는지 저장 : complete
    complete = len(cakes)
    while complete != 1:
        # [ 0 ~ complete -1 ] 중에서 max 찾기
        some_cake = cakes[0:complete]
        max_idx = some_cake.index(max(some_cake))
        if max_idx != complete - 1:
            # [ 0 ~ max_idx ] 범위 flip
            if max_idx != 0:
                flip(max_idx)
            # [ 0 ~ complete - 1 ] 범위 flip
            # 이때 0에는 최댓값이 들어가있다.
            flip(complete - 1)
        complete -= 1
    # 출력부
    print(" ".join(map(str, answer)))

    T -= 1
