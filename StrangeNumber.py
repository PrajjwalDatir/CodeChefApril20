from sys import stdin


def strange_number():
    X, K = map(int, stdin.readline().split())
    if X < K:
        print("0")
    elif K == 0:
        if X == 1:
            print("1")
        else:
            print("0")
    else:
        if X > (pow(2, K) - 1):
            print("1")
        else:
            print("0")


T = int(stdin.readline())
for t in range(T):
    strange_number()

'''

'''
