# -*- coding: utf-8 -*-
"""
Charles Truscott Watters
USanDiego MicroMasters 
runfile('C:/Users/Charles/Desktop/change.py', wdir='C:/Users/Charles/Desktop')
monetary_value: 3 coins: [2, 2, 0.5, 0.25, 0.25] denominations: [[2, 1]]
monetary_value: 1 coins: [2, 2, 0.5, 0.25, 0.25] denominations: [[2, 1], [2, 1]]
monetary_value: 0.5 coins: [2, 2, 0.5, 0.25, 0.25] denominations: [[2, 1], [2, 1], [0.5, 1]]
monetary_value: 0.25 coins: [2, 2, 0.5, 0.25, 0.25] denominations: [[2, 1], [2, 1], [0.5, 1], [0.25, 1]]
monetary_value: 0.0 coins: [2, 2, 0.5, 0.25, 0.25] denominations: [[2, 1], [2, 1], [0.5, 1], [0.25, 1], [0.25, 1]]
Denominations: [[2, 1], [2, 1], [0.5, 1], [0.25, 1], [0.25, 1]]
i: 2 r: 1 denominations: [[2, 2]]
i: 0 r: 1 denominations: [[2, 2], [2, 0]]
i: 2.0 r: 0.0 denominations: [[2, 2], [2, 0], [0.5, 2.0]]
i: 0.0 r: 0.0 denominations: [[2, 2], [2, 0], [0.5, 2.0], [0.25, 0.0]]
i: 0.0 r: 0.0 denominations: [[2, 2], [2, 0], [0.5, 2.0], [0.25, 0.0], [0.25, 0.0]]
Denominations: [[2, 2], [2, 0], [0.5, 2.0], [0.25, 0.0], [0.25, 0.0]]
Charles Truscott Watters, USanDiego `Algorithms and Data Structures MicroMasters` edX.org C. 1 Kulikov, Pevzner et alia

"""

def change_simple(monetary_value = 5, coins = [], denominations = []):
    while monetary_value > 0:
        for coin in coins:
            monetary_value -= coin
            denominations.append([coin, 1])

            print("monetary_value: {} coins: {} denominations: {}".format(monetary_value, coins, denominations))
    print("Denominations: {}".format(denominations))
    return denominations
            
            
def change_efficient(monetary_value = 10, coins = [], denominations = []):
    r = monetary_value
    for coin in coins:
        i = r // coin
        r = r - coin * i
        denominations.append([coin, i])
        print("i: {} r: {} denominations: {}".format(i, r, denominations))
    print("Denominations: {}".format(denominations))
    return denominations

def main():
    change_simple(5, [2, 2, .50, .25, .25])
    change_efficient(5, [2, 2, .50, .25, .25])
    print("Charles Truscott Watters, USanDiego `Algorithms and Data Structures MicroMasters` edX.org C. 1 Kulikov, Pevzner et alia")
if __name__ == "__main__": main()