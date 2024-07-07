
m, n = map(int, input().split())

nums = []
for i in range(m):
  cards = list(map(int, input().split()))
  nums.append(min(cards))
print(max(nums))