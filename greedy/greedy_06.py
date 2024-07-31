from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
data = list(map(int, input().split()))
_n = int(n)
_m = int(m)
data.sort()

res = 0
i = 0
while True:
  x = data[i]
  rig = bisect_right(data, x)
  lef = bisect_left(data, x)
  res += (len(data) - rig) * (rig - lef)
  #print(i, x, lef, rig, res)
  i = rig
  if i == n :
    break
print(res)