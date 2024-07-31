data = input()

row = int(data[1])
col = int(ord(data[0])) - int(ord('a')) + 1
#ord 라는 함수는 str 변수를 아스키 코드로 변경해준다
#뺄셈 연산을 위해서 int 로 바꿔준다
#0부터 7이 아니라 1부터 8로 만들어주기 위해서 1을 더한다

res=0
dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]
#이 방법 외에
#steps = [(-2, -1), (-1, -2)...] 처럼 방향벡터를 정의해서 풀 수도 있다

for step in range(8):
  new_x = row + dx[step]
  new_y = col + dy[step]
  if new_x >= 1 and new_x <= 8 and new_y >=1 and new_y <= 8:
    res += 1
    
print(res)
      