i,j,k = map(int,input().split())
sum = 0
for n in range(1,k+1):
  sum += (i+(n-1)*j)
print(sum)
