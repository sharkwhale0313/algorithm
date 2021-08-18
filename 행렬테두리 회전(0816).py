

def solution(rows, columns, queries):
    answer = []
    matrix = [[row * columns + col + 1 for col in range(columns)] for row in range(rows)]
    for x1, y1, x2, y2 in queries:
        first = matrix[x1-1][y1-1]
        mini = first

        for k in range(x1-1, x2-1):  # 왼쪽 세로
            tmp = matrix[k+1][y1-1]
            matrix[k][y1-1] = tmp
            mini = min(mini, tmp)

        for k in range(y1-1, y2-1):  # 하단 가로
            tmp = matrix[x2-1][k+1]
            matrix[x2-1][k] = tmp
            mini = min(mini, tmp)

        for k in range(x2-1, x1-1, -1):  # 왼쪽 세로
            tmp = matrix[k-1][y2-1]
            matrix[k][y2-1] = tmp
            mini = min(mini, tmp)

        for k in range(y2-1, y1-1, -1):  # 상단 가로
            tmp = matrix[x1-1][k-1]
            matrix[x1-1][k] = tmp
            mini = min(mini, tmp)
            
        matrix[x1-1][y1] = first
        answer.append(mini)

    return answer
