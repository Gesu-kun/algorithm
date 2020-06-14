import sys


def int1(x): return int(x) - 1
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def mi1(): return map(int1, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def lli(rows_number): return [li() for _ in range(rows_number)]


if __name__ == "__main__":
    x, n = mi()
    if n == 0:
        print(x)
        exit()
    p_l = li()
    a = list(range(0, 1000))
    for p in p_l:
        a.remove(p)
    ans = 0
    min_dif = 10000
    for i in a:
        dif = abs(i-x)
        if dif < min_dif:
            min_dif = dif
            ans = i
    print(ans)
