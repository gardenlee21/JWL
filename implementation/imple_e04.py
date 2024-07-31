N, M = map(int, input().split())
x, y, direction = map(int, input().split())

array = []
for i in range(N):
  array.append(list(map(int, input().split())))
#map 을 하고나면 따로따로 되어있으니까 list 처리를 해줘야 한다
#input 받기 끝

#북,동,남,서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#방문한 위치를 저장하기 위한 맵 N X M 을 만들어서 0으로 초기화
d = [[0] * M for _ in range(N)]
d[x][y] = 1

def turn_left(): #북-동-남-서
  global direction
  direction -= 1
  if direction == -1: 
    direction = 3 #서

#시뮬레이션 시작
count = 1
turn_time = 0

while True:
  turn_left()#direction 을 왼쪽으로 회전
  nx = x + dx[direction]
  ny = y + dy[direction]
  
  #회전했더니 가보지 않은 칸이 있다면 = 육지면서 방문한적 없어야 함
  if array[nx][ny] == 0 and d[nx][ny] == 0:
    d[nx][ny] = 1 #앞으로 전진!
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
    
  #회전했더니 앞이 바다거나 가보지 않은 칸이 없을 경우
  else:
    turn_time += 1
  
  if turn_time == 4: #네 방향 모두 갈 수 없는 경우
    nx = x - dx[direction]
    ny = y - dy[direction]
    #한칸 뒤로 갈수 있으면 = 육지면 가기
    if array[nx][ny] == 0:
      x = nx
      y = ny
    #못가는 경우 (바다로 막혀있는 경우)
    else:
      break
    turn_time = 0

print(count)
  