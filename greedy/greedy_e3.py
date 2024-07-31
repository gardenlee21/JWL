n, k = list(map(int, input().split()))

count = 0

while True:
  # N 이 K 로 나누어 떨어질 때까지 1씩 빼기
  target = (n//k)*k
  count += (n-target) #1 다 뺐음
  print(target)
  n = target
  #N 이 K 보다 작을 때 (더이상 나눌 수 없을 때) 반복문 탈출
  print(n, count)
  if n < k:
    break
  n //= k
  count += 1

count += n-1
print(count)