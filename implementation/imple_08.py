data = list(input())

alpha = []
num = []
for d in data:
  if ord(d) >= ord('A'):
    alpha.append(int(ord(d)))
  else:
    num.append(int(d))

alpha.sort()
num_sum = sum(num)

res = []
for a in alpha:
  res.append(chr(a))
  
res.append(str(num_sum))

print(''.join(res)) 
