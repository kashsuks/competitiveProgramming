import sys
import math

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

class Solution:
    def solve(self):
        # Your code here
        pass

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    t = int(input_data[idx])
    idx += 1
    results = []
    solution = Solution()
    
    while t > 0:
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        results.append(a + b)
        idx += 2
        t -= 1
    
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()
