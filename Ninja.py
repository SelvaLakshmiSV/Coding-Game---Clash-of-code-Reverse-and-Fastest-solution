import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

mmm, aaa, nnn = [int(i) for i in input().split()]
z =  -aaa + (nnn*(nnn+1))//2 * mmm
print( z * (z > 0))
