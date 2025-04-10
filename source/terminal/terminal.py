
import time
from source.sorting.sorting import sorting_algorithms

def run_terminal_interface():
    print("Welcome to the Papyri sort")
    print("Choose an algorithm sort :")

    for key in sorting_algorithms:
        print(f"- {key}")

    algo_name = input("Algorithm name : ").strip().lower()

    if algo_name not in sorting_algorithms:
        print("Algorithm not found")
        return

    try:
        input_str = input("Enter a list of numbers to sort :\nExample → 10, 5, 3, 8\n> ")
        user_list = [float(x.strip()) for x in input_str.split(",")]
    except ValueError:
        print("Invalid format, please retry")
        return

    tri = sorting_algorithms[algo_name]

    start_time = time.perf_counter()
    result = tri(user_list)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    print(f"\nResult, list sorted '{algo_name}' : {result}")
    print(f"Time to be sorted : {elapsed_time:.6f} seconds")
