import io
import sys

_INPUT = """\
6
5 3
1 2 4 8 16
20 10
100000000 100000000 98667799 100000000 100000000 100000000 100000000 99986657 100000000 100000000 100000000 100000000 100000000 98995577 100000000 100000000 99999876 100000000 100000000 99999999
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,K=map(int,input().split())
  A=list(map(int,input().split()))
  ans=sum(A)*(N-K+1)
  for i in range(N-K):
    ans-=(N-K-i)*(A[i]+A[N-i-1])
  print(ans)