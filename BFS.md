## BFS (Breadth First Search) 너비 우선 탐색

1. BFS vs DFS
##### 대표적인 그래프 탐색 알고리즘
> BFS, DFS 는 둘 다 그래프를 탐색하는 방법이다.
> 그래프를 탐색하는 법에는 BFS, DFS 두가지 종류가 있다.
> 너비 우선 탐색 BFS : 정점들과 같은 레벨에 있는 노드들 (형제 노드들)을 먼저 탐색하는 방식
> 깊이 우선 탐색 DFS : 정점의 자식들을 먼저 탐색하는 방식
![im1]./image/im1.png
BFS : A - B - C - D - G - H - I - E - F - J
→ 한 단계씩 내려가면서, 해당 노드와 같은 레벨에 있는 노드들을 먼저 순회

DFS : A - B - D - E - F - C - G - H - I - J
→ 한 노드의 자식을 타고 끝까지 순회한 후에, 다시 돌아와서 다른 형제들의 자식을 타고 내려가며 순회함

##### python 으로 그래프 구현
![im2]./image/im2.png
```
# 딕셔너리와 리스트를 통해 구현 가능
graph = dict()

graph['A'] = ['B','C']
graph['B'] = ['A','D']
graph['C'] = ['A','G','H','I']
graph['D'] = ['B','E','F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C','J']
graph['J'] = ['I']
```

![im3]./image/im3.png
need_visit queue에 제일 앞에있는 노드를 넣음
visited queue 에 큐의 정책(FIFO)에 따라 데이터를 하나하나 꺼내서 방문
visited queue에 이미 있다면 아무것도 안하고 끝남

##### BFS 알고리즘 구현
> Queue 를 활용
> > need_visit queue, visited queue : 2개의 큐를 생성해서 관리
```
def bfs(graph, start_node):
	visited = list()
	need_visit = list()
	
	# need_visit에 start_node를 넣으면서 시작
	need_visit.append(start_node)

	while need_visit:
		node = need_visit.pop(0) # pop은 가장 뒤에있는 것 부터 빼지만 index를 명시하면 됨
		if node not in visited:
			visited.append(node)
			need_visit.extend(graph[node]) # append 와 extend 는 다름
			# append [1, 2, [3, 4]]
			# extend [1, 2, 3, 4]]
	
	return visited

```
```
bfs(graph, 'A')
```
##### 시간복잡도
> 일반적인 BFS 시간 복잡도
> > - 노드 수 : V
> > - 간선 수 : E
> > - 위 코드에서 while need_visit 은 V + E 번 만큼 수행함
> > - 시간 복잡도 → O(V + E)
