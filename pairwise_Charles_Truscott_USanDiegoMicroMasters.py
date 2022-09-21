# -*- coding: utf-8 -*-
"""
Charles Truscott
USanDiego MicroMasters `Algorithms and Data Structures MicroMasters`
Attempt #2
6
10 20 30 309 800 200
The maximum pairwise product of [10, 20, 30, 309, 800, 200] is 247200
Charles Truscott Watters for a USanDiego MicroMasters unit
Press any key to continue . . .
"""
import math
def max_pairwise_product(n):
    """ Charles Truscott Watters, Byron Bay NSW 2481 """
    if len(n) < 1000:
        s = 0
        prev_s = 0
        ans = 0
        for i in range(0, len(n) - 1, 1):
            for j in range(1, n[i], 1):
                s = 0
                for k in range(0, n[i]):
                    s += n[i + 1]
                if s > prev_s:
                    ans = s
#                print("k: {}, n[i + 1]: {} i: {} j: {} s: {} prev_s: {}".format(k, n[i + 1], i, j, s, prev_s))
            prev_s = s
        print("The maximum pairwise product of {} is {}".format(n, ans))
        return ans
        
        


def main():
    # Charles Truscott Watters, thank you edX and instructors from USanDiego
    x = int(input())
    y = input().split(' ')
    z = []
    for num in y:
        z.append(int(num))

#    print(z)
    max_pairwise_product(z)
    print("Charles Truscott Watters for a USanDiego MicroMasters unit")
    
    
    
if __name__ == "__main__": main()
