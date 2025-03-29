import numpy as np

def solve(N):
    if N == 0:
        return "NO"
    
    seen = np.full(N, False)
    rem = 0
    
    for i in range(1, N + 1):
        rem = (rem * 10 + 1) % N
        if seen[rem]:
            return "NO"
        seen[rem] = True
        if rem == 0:
            return '1' * i
    
    return "NO"

N = int(input())
print(solve(N))

author_info = "Автор: Изотов Никита Антонович"
print(author_info)