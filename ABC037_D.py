import io
import sys

_INPUT = """\
6
2 3
1 4 5
2 4 9
6 6
1 3 4 6 7 5
1 2 4 8 8 7
2 7 9 2 7 2
9 4 2 7 6 5
2 8 4 6 7 6
3 7 9 1 2 7
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  import sys
  sys.setrecursionlimit(1000000)
  mod=10**9+7
  H,W=map(int,input().split())
  A=[list(map(int,input().split())) for _ in range(H)]
  memo=[-1]*(H*W)
  def rec(k):
    if memo[k]!=-1: return memo[k]
    memo[k]=1
    i,j=k//W, k%W
    for ii,jj in [[i-1,j],[i,j-1],[i+1,j],[i,j+1]]:
      if 0<=ii<H and 0<=jj<W and A[ii][jj]>A[i][j]: memo[k]=(memo[k]+rec(ii*W+jj))%mod
    return memo[k]
  ans=0
  for k in range(H*W): ans=(ans+rec(k))%mod
  print(ans)