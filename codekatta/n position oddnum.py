i,j=map(int,input().split())
lis=[int(x) for x in input()]
c=0
for k in lis:
  if(k%2!=0):
    c=c+1
    if(c==j):
      print(k)
