# -*- coding: utf-8 -*-
"""
Charles Truscott
USanDiego MicroMasters `Algorithms and Data Structures MicroMasters`
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
                print("k: {}, n[i] + 1: {} i: {} j: {} s: {} prev_s: {}".format(k, n[i+ 1], i, j, s, prev_s))
            prev_s = s
        print("{}".format(s))
        return s
        
        


def main():
    # Charles Truscott Watters, thank you edX and instructors from USanDiego
    x = int(input())
    y = input().split(' ')
    z = []
    for num in y:
        z.append(int(num))

#    print(z)
    max_pairwise_product(z)
    
    
    
if __name__ == "__main__": main()
