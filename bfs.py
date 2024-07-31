from collections import deque

def bfs(graph, start, visited):
  #큐 구현을 위해 deque 라이브러리 사용
  queue = deque([start]) #큐에 start 노드 삽입
  #현재 노드 방문처리 (start 노드)
  visited[start] = True
  #큐가 텅 빌때까지 반복
  while queue:
    #큐에서 하나의 노드를 뽑아 출력하기
    v = queue.popleft()
    print(v, end=' ')
    #뽑은 노드의 인접한 노드들 중 방문하지 않은 노드들 모두 큐에 삽입하고, 방문 처리하기
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True



graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]
#인접 리스트
#보통 인덱스가 1부터 주어지기 때문에 인덱스 0은 비워둠

visited = [False] * 9
#1-8까지 주어졌지만 인덱스0을 비웠으니 총 9개 필요

bfs(graph, 1, visited)