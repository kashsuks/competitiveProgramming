import sys
import math

#Start of Kashyap Sukshavasi's template for CP
input = sys.stdin.read
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
#End of Kashyap Sukshavasi's template for CP

def main():
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    while t > 0:
        a = int(data[idx])
        b = int(data[idx+1])
        results.append(a + b)
        idx += 2
        t -= 1
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()
