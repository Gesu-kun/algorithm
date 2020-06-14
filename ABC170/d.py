import sys
import math


def int1(x): return int(x) - 1
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def mi1(): return map(int1, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def lli(rows_number): return [li() for _ in range(rows_number)]


if __name__ == "__main__":
    n = ii()
    a = li()
    a = sorted(list(set(a)))
    b = [True] * (a[-1] + 1)
    def sived(x):
        for not_ans in range(x+x, a[-1]+1, x):
            b[not_ans] = False
    for i in range(a[0]):
        b[i] = False
    for i in a:
        if b[i-1]:
            sived(i)
    ans = 0
    for i in a:
        if b[i-1]:
            ans += 1
    print(ans-1)
