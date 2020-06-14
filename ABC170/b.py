import sys


def int1(x): return int(x) - 1
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def mi1(): return map(int1, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def lli(rows_number): return [li() for _ in range(rows_number)]


if __name__ == "__main__":
    x, y = mi()
    tks = []
    for i in range(x+1):
        tks.append([i, x-i])
    for tk in tks:
        if tk[0]*2 + tk[1]*4 == y:
            print('Yes')
            exit()
    print('No')
