n,m= map(int,input().split())
set1={int(x) for x in input().split()}
set2={int(y) for y in input().split()}
if((set2.issubset(set1))):
  print("YES")
else:
  print("NO")
