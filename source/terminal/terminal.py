# source/terminal/terminal.py

import time
from source.sorting.sorting import sorting_algorithms

def run_terminal_interface():
    print("📚 Bienvenue dans le trieur de papyrus d'Héron !")
    print("Choisissez un algorithme de tri :")

    for key in sorting_algorithms:
        print(f"- {key}")

    algo_name = input("Nom de l’algorithme : ").strip().lower()

    if algo_name not in sorting_algorithms:
        print("❌ Algorithme non reconnu.")
        return

    try:
        input_str = input("Entrez une liste de nombres séparés par des virgules :\nExemple → 10, 5, 3, 8\n> ")
        user_list = [float(x.strip()) for x in input_str.split(",")]
    except ValueError:
        print("❌ Format invalide. Veuillez entrer uniquement des nombres.")
        return

    tri = sorting_algorithms[algo_name]

    # Chronométrage du tri
    start_time = time.perf_counter()
    result = tri(user_list)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    print(f"\n✅ Résultat trié avec '{algo_name}' : {result}")
    print(f"⏱️ Temps d'exécution : {elapsed_time:.6f} secondes")
