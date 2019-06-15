a,d,n=map(int,input().split())
p=0
for i in range(0,n+1):
  p=p+(a+(i-1)*d)
print(p)
