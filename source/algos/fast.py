import random

def partition(lst,bot,top):
    pivot = random.choice(lst)
    i = bot - 1
    for j in range(bot,top):
        if lst[j] < pivot:
            i = i + 1
            lst[j],lst[i] = lst[i],lst[j]
    lst[i+1],lst[top] = lst[top],lst[i+1]
    return i + 1

def fast(lst,bot,top):
    if bot < top:
        pi = partition(lst,bot,top)
        fast(lst,bot,pi-1)
        fast(lst,pi+1,top)
