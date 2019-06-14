n=int(input())
lis=[int(x) for x in input().split()]
lis.sort()
for i in range(n-1,-1,-1):
  print(lis[i],end='')
