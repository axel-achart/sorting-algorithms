# test_sort.py (à la racine ou dans un dossier temporaire)

from source.algos.selection_sort import selection_sort
from source.algos.bubble_sort import bubble_sort

liste_test = [29, 10, 14, 37, 13]

print("Tri par sélection :", selection_sort(liste_test))
print("Tri à bulles     :", bubble_sort(liste_test))
