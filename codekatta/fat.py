n=int(input())
if(n==0):
   print("1")
else:
    p=1
    for i in range(1,n+1):
        p=p*i
    print(p)
