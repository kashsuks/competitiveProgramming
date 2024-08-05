import sys
import math
from collections import defaultdict, deque
from itertools import permutations, combinations
from functools import lru_cache
from heapq import heappush, heappop

# Constants
MOD = 1_000_000_007

# Shortcuts for I/O
input = sys.stdin.read
def inp(): return input().strip()
def inps(): return input().split()
def intinp(): return int(input().strip())
def intinps(): return map(int, input().strip().split())
def intinpl(): return list(map(int, input().strip().split()))

# Useful functions
def gcd(a, b): return math.gcd(a, b)
def lcm(a, b): return (a * b) // gcd(a, b)

# Shortcuts
def pr(*args): print(" ".join(map(str, args)))
def prl(arr): print(" ".join(map(str, arr)))
def prll(arr): print("\n".join(map(str, arr)))

# Aliases for common data structures
ii = lambda: int(input().strip())
mi = lambda: list(map(int, input().strip().split()))
ss = lambda: input().strip()

# Loops
def forn(n): return range(n)
def f(i, s, e): return range(s, e)
def cf(i, s, e): return range(s, e + 1)
def rf(i, e, s): return range(e - 1, s - 1, -1)

# Main solve function
def solve():
    # Write code here
    pass

# Driver code
def main():
    t = intinp()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
