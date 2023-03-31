import time
from collections import defaultdict
import nntplib


def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = int(input())
    

    parents = [0] * (N + 1)
    for i, p in enumerate(P, 2):
        parents[i] = p
    
    for _ in range(Q):
        query = list(map(int, input().split()))
        
        if query[0] == 1:
            u, v = query[1], query[2]
            parents[u] = v
        elif query[0] == 2:
            x = query[1]
            while parents[x] != 0 and parents[x] < x:
                x = parents[x]
            print(x)

if __name__ == '__main__':
    main()
