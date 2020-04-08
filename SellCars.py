# chef wants to Sell all the cars
import sys


def sell_cars():
    total_cars = int(sys.stdin.readline())
    price_list = list(sys.stdin.readline().split())
    # print(sorted(price_list))
    profit = 0
    price_list.sort(key=int, reverse=True)
    # print(price_list)
    for i in range(total_cars):
        cash = (int(price_list[i]) - i)
        # print(cash)
        if cash < 0:
            cash = 0
        profit = profit + cash
    print(profit % 1000000007)


T = int(sys.stdin.readline())
for t in range(T):
    sell_cars()  # To call the sell cars function T number of times
