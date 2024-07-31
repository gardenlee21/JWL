n = int(input())

res = 0
check = [3, 13, 23, 33, 43, 53, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]

for hour in range(n+1):
  for min in range(60):
    for sec in range(60):
      if hour in check or min in check or sec in check:
        res += 1

print(res)