import heapq  # 우선순위 큐 구현을 위함


def dijkstra(n, start, end, roads, traps):
    answer = 0
    traps_index = {value: ind for ind, value in enumerate(traps)}
    state_table = [[0 for _ in range(n + 1)] for _ in range(1 << len(traps))]
    graph = {}
    for road in roads:
        graph[road[0]][road[1]] = [road[2], 0]
        graph[road[1]][road[0]] = [road[2], 1]
    queue = []
    heapq.heappush(queue, [0, start, 0])  # 시작 노드부터 탐색 시작 하기 위함.
    state_table[0][start] = 0  # 시작 값은 0

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        current_distance, current_destination, state = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.
        if end == current_destination:  # 도착했다면 끝내기
            answer = current_distance
            break
        if state_table[state][current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue

        connected_nodes = []  # 상태가 같은 경우에만 고려하는 경로에 넣음
        for connected_node, connected_distance in graph[current_destination].items():
            if state_table[state][current_destination] == connected_distance[1]:  # dp에서 지금 어떤 상태인지 가져옴
                connected_nodes.append([connected_node,connected_distance])

        for new_destination, new_distance in connected_nodes:
            distance = current_distance + new_distance[0]  # 해당 노드를 거쳐 갈 때 거리
            if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                distances[new_destination] = distance
                if new_destination in traps:
                    # state 를 지금 밟은 trap을 xor한 것으로 바꿔줌
                    heapq.heappush(queue, [distance, new_destination, state_list[new_destination]])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
                else:
                    heapq.heappush(queue, [distance, new_destination, 0)  # 다음 인접 거리를 계산 하기 위해 큐에 삽입

    return answer