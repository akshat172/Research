#!/bin/python

import sys
import os

# Complete the function below.
import math
def triangleOrNot(a, b, c):
    res = []
    if 1<= len(a)<= pow(10,5) and 1<= len(b)<= pow(10,5) and 1 <= len(c)<= pow(10,5):
        for i in range(0,len(a)):
            if 1 <= a[i] <= pow(10,3) and 1 <= b[i] <= pow(10,3) and 1 <= c[i] <= pow(10,3) and 0<=i <len(a):
                if (a[i] > b[i] + c[i] or a[i] == b[i] + c[i]) or (b[i] > a[i] + c[i] or b[i] == a[i]+c[i]) or (c[i] >a[i] + b[i] or c[i] == a[i]+b[i]):
                    res.append('No')
                else:
                    res.append('Yes')
    return res

if __name__ == "__main__":
    f = open(os.environ['OUTPUT_PATH'], 'w')
    a_cnt = 0
    a_cnt = int(raw_input())
    a_i = 0
    a = []
    while a_i < a_cnt:
        a_item = int(raw_input());
        a.append(a_item)
        a_i += 1


    b_cnt = 0
    b_cnt = int(raw_input())
    b_i = 0
    b = []
    while b_i < b_cnt:
        b_item = int(raw_input());
        b.append(b_item)
        b_i += 1


    c_cnt = 0
    c_cnt = int(raw_input())
    c_i = 0
    c = []
    while c_i < c_cnt:
        c_item = int(raw_input());
        c.append(c_item)
        c_i += 1


    res = triangleOrNot(a, b, c);
    for res_cur in res:
        f.write( str(res_cur) + "\n" )

    f.close()