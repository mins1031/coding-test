import sys
from itertools import permutations

n, s = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

tmp = list(permutations(array))
print(tmp)

#  아직 다 못함