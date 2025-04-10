def insertion(lst):

    sorted_lst = lst.copy()
    n = len(sorted_lst)

    for i in range(1,n):

        key = sorted_lst[i]
        j = i -1
        while j >= 0 and sorted_lst[j] > key:

            sorted_lst[j+1] = sorted_lst[j]
            j = j - 1

        sorted_lst[j + 1] = key
    
    return sorted_lst