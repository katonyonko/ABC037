import io
import sys

_INPUT = """\
6
5 2
1 3 10
2 4 20
10 4
2 7 22
3 5 4
6 10 1
4 4 12
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,Q=map(int,input().split())
  ans=[0]*N
  for i in range(Q):
    L,R,T=map(int,input().split())
    for j in range(L-1,R): ans[j]=T
  print(*ans,sep='\n')