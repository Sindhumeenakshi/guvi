t,l=input().split()
t=int(t)
l=int(l)
for i in range(t+1,l):
  if(i>1):
    for j in range(2,i):
      if(i%j==0):
        break

    else:
      print(i,end=' ')
  else:
    break
