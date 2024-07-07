data = input()

#0으로 다 바꾸는 경우와 1로 다 바꾸는 경우를 비교해서 작은 거를 출력한다

count0 = 0 #0으로 바꾸는 경우
count1 = 0 #1로 바꾸는 경우

#먼저 첫번째 원소에 대해 생각
if data[0] == '1':
  count0 += 1
else:
  count1 += 1

for i in range(len(data) - 1):
  if data[i] != data[i+1]:
    if data[i+1] == '1': #다음 수에서 1로 바뀌는 경우
      count0 += 1
    else: #다음 수에서 0으로 바뀌는 경우
      count1 += 1

print(min(count0, count1))