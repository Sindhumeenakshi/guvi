K=int(input())
n=list(map(int,input().split()))
li=[]
for x in range(K):
    for i in range(x+1,len(n)):
        if(n[i]==n[x]):
          li.append(n[x])

li.sort()
li2=set(li)
for x in li2:
  print(x,end=" ")
