# source/algos/bubble_sort.py

def bubble_sort(lst):
    """
    Trie une liste de nombres en utilisant l'algorithme de tri à bulles.
    
    Paramètres :
        lst (list) : Liste de nombres à trier.
        
    Retour :
        list : Nouvelle liste triée.
    """
    sorted_lst = lst.copy()  # On ne modifie pas la liste originale
    n = len(sorted_lst)

    for i in range(n):
        # Optimisation : on vérifie si la liste est déjà triée
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_lst[j] > sorted_lst[j + 1]:
                # Échange des éléments
                sorted_lst[j], sorted_lst[j + 1] = sorted_lst[j + 1], sorted_lst[j]
                swapped = True
        if not swapped:
            break  # Si aucun échange, la liste est déjà triée
    
    return sorted_lst
