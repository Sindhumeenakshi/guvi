i=int(input())
lis=[int(x)for x in  input().split()]
li=[lis.sort()]
for i in lis:
  for j in li:
    if(i!=j):
      d=1
      
if(d==1): 
  print(lis.index(i))
  
