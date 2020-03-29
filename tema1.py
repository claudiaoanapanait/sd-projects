from random import shuffle
import random
import time

# FUNCTIE TIMER
def timing(f):
    def wrap(*args):
        time1 = time.time()
        f(*args)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2-time1)*1000.0))
    return wrap

# BUBBLE SORT
@timing
def bubblesort(l):
    ok = 1
    n=len(l)
    for i in range(n - 2):
        if l[i] > l[i + 1]:
            ok = 0
            a = l[i]
            l[i] = l[i + 1]
            l[i + 1] = a
    if ok == 0:
        bubblesort(l)


# COUNT SORT
@timing
def countsort(l):
    maxi = max(l)
    v = [0] * (maxi + 1)
    n=len(l)
    for i in range(n):
        v[l[i]] += 1
    for i in range(1, maxi + 1):
        v[i] = v[i - 1] + v[i]
    sol = [0] * n
    for i in range(n):
        sol[v[l[i]] - 1] = l[i]
        v[l[i]] += -1
    for i in range(n):
        l[i] = sol[i]


# RADIX SORT
@timing
def radixsort(l):
    max1 = max(l)
    exp1 = 1
    while max1 / exp1 > 0:
        countsorting(l, exp1)
        exp1 = exp1 * 10
def countsorting(l, exp1):
    v = [0] * 10
    n=len(l)
    for i in range(n):
        index = int((l[i] / exp1) % 10)
        v[index] += 1
    for i in range(1, 10):
        v[i] = v[i - 1] + v[i]
    sol = [0] * n
    for i in range(n - 1, -1, -1):
        index = int((l[i] / exp1) % 10)
        sol[v[index] - 1] = l[i]
        v[index] += -1
    for i in range(n):
        l[i] = sol[i]


# MERGE SORT
@timing
def mergesort(l):
    n = len(l)
    if n > 1:
        mid = n // 2
        L = l[:mid]
        R = l[mid:]
        mergesort(L)
        mergesort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                l[k] = L[i]
                i += 1
            else:
                l[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            l[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            l[k] = R[j]
            j += 1
            k += 1


# QUICK SORT
@timing
def quicksort(l, start, stop):
    if start<stop:
        pi=partition_r(l, start, stop)
        quicksort(l, pi-1, stop)
        quicksort(l, pi+1, stop)
def partition_r(l, start, stop):
    r=random.randrange(start, stop)
    l[r],l[stop]=l[stop],l[r]
    return partition (l, start, stop)
def partition(l, start, stop):
    pivot=l[stop]
    i=start
    for j in range (start, stop):
        if l[j]<=pivot:
            i+=1
            l[i], l[j]= l[j], l[i]

    l[i], l[stop]=l[stop], l[i]
    return i

# PROGRAM PRINCIPAL
lun = [10, 100, 1000, 10000, 100000]
for n in lun:
    print("N=", n)
    print("Max=", n)
    x = [j for j in range(10)]
    shuffle(x)
    bubblesort(x)
    shuffle(x)
    countsort(x)
    shuffle(x)
    radixsort(x)
    shuffle(x)
    mergesort(x)
    shuffle(x)
    quicksort(x)




