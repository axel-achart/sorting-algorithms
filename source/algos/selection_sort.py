# source/algos/selection_sort.py

def selection_sort(lst):
    """
    Trie une liste de nombres en utilisant l'algorithme de tri par sélection.
    
    Paramètres :
        lst (list) : Liste de nombres à trier.
        
    Retour :
        list : Nouvelle liste triée.
    """
    sorted_lst = lst.copy()  # On ne modifie pas la liste originale
    n = len(sorted_lst)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if sorted_lst[j] < sorted_lst[min_index]:
                min_index = j
        # Échange
        sorted_lst[i], sorted_lst[min_index] = sorted_lst[min_index], sorted_lst[i]
    
    return sorted_lst
