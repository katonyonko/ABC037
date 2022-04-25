import io
import sys

_INPUT = """\
6
3 5 6
8 6 20
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A,B,C=map(int,input().split())
  print(C//min(A,B))