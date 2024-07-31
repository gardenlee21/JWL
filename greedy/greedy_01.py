n = map(int, input())
peo = list(map(int, input().split()))

peo.sort() #오름차순

result = 0 # 그룹 수

count = 0 # 현재 그룹에 포함된 모험가 수
for i in peo: #공포도 낮은 것 부터 하나씩 체크
  count += 1
  if i <= count:
    result += 1 #현재 팀원의 공포도가 그룹원 수보다 작거나 같은 경우 그룹을 결성한다
    count = 0 #현재 그룹에 포함된 그룹원 수 초기화

print(result)



