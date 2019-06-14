m,n=input().split()
m=int(m)
n=int(n)
c=0
for i in range(m,n):
  if(i>1):
    for j in range(2,i):
      if(i%j==0):
        break

    else:
      c=c+1
  else:
    break
print(c)
