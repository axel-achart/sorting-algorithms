
def comb_sort(lst):
    sorted_lst = lst.copy() 
    n = len(sorted_lst)
    gap = n
    shrink = 1.3 
    swapped = True

    while gap > 1 or swapped:

        gap = int(gap / shrink)
        if gap < 1:
            gap = 1 

        swapped = False

        for i in range(n - gap):
            if sorted_lst[i] > sorted_lst[i + gap]:
                sorted_lst[i], sorted_lst[i + gap] = sorted_lst[i + gap], sorted_lst[i]
                swapped = True 

    return sorted_lst
