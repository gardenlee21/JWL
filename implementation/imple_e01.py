n = int(input())
plans = input().split()

#처음 시작점
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']

nx, ny = 0, 0
for plan in plans:
  #이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  #공간을 벗어나는 경우 무시하기
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  x, y = nx, ny

print(x, y)