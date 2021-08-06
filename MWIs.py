#!/usr/bin/env python3

textFile = open("MWIS.txt","r")
lines = textFile.read().split("\n")

lines = [int(i) for i in lines]
#print(lines)

def mwis(w):
    n=len(w)
    a=[0, w[0]]
    print(a)
    for i in range(2, n+1):
        a.append(max(a[i-1], a[i-2]+w[i-1]))
    print(a)
    i = n
    s = set()
    while i >= 1:
        if a[i] == a[i-1]:
            i-=1
        else:
            s.add(i-1)
            i-=2
    return s

print(mwis(lines))