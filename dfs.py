def dfs(graph, v, visited):
  #현재 노드 방문 처리
  visited[v] = True
  print(v, end=' ')#프린트할때 끝에 ' ' 붙이기
  #현재 노드와 연결된 다른 노드를 재귀적으로 방문하기
  for i in graph[v]:
    if not visited[i]: #방문하지 않은 노드만 방문하기
      dfs(graph, i, visited)


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

dfs(graph, 1, visited)
