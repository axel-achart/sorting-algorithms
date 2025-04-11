
from config import *
import tkinter as tk
import random
import time
import json
from datetime import datetime
import matplotlib.pyplot as plt

from source.algos.selection_sort import selection_sort
from source.algos.bubble_sort import bubble_sort
from source.algos.insertion import insertion
from source.algos.heapsort import heapsort_sort
from source.algos.fusion import fusion_sort
from source.algos.fast import fast
from source.algos.comb_sort import comb_sort

algorithms = {
    "Selection Sort": selection_sort,
    "Bubble Sort": bubble_sort,
    "Comb Sort": comb_sort,
    "Fast Sort": fast,
    "Insertion Sort":insertion,
    "Fusion Sort": fusion_sort,
    "Heap Sort": heapsort_sort
}

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualisation Algorithms Sort")
        self.canvas = tk.Canvas(root, width=ROOT_WIDTH, height=ROOT_HEIGHT, bg=BACKGROUND)
        self.canvas.pack(padx=10, pady=10)
        self.execution_times = {}
        
        control_frame = tk.Frame(root)
        control_frame.pack()

        self.algo_var = tk.StringVar(value="Bubble Sort")
        tk.OptionMenu(control_frame, self.algo_var, *algorithms.keys()).pack(side=tk.LEFT, padx=5)

        tk.Button(control_frame, text="New List", command=self.generate_data).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Launch Sort", command=self.run_sort).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="View History", command=self.show_history).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Compare times", command=self.plot_execution_times).pack(side=tk.LEFT, padx=5)

        self.time_label = tk.Label(root, text="Time to sort : 0.000000 s", font=FONT)
        self.time_label.pack(pady=5)

        self.list_size = tk.IntVar(value=50)
        tk.Label(control_frame, text="List Size").pack(side=tk.LEFT, padx=5)
        tk.Scale(control_frame, from_=10, to=100, orient=tk.HORIZONTAL, variable=self.list_size).pack(side=tk.LEFT, padx=5)


        self.generate_data()

    def generate_data(self):
        size = self.list_size.get()
        self.original_data = [random.randint(10, 390) for _ in range(size)]
        self.data = self.original_data.copy()
        self.draw_data(self.data)


    def draw_data(self, data, color=COLOR_ONE):
        self.canvas.delete("all")
        width = 800 / len(data)
        for i, value in enumerate(data):
            x0 = i * width
            y0 = 400 - value
            x1 = (i + 1) * width
            y1 = 400
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        self.root.update_idletasks()

    def run_sort(self):
        algo_name = self.algo_var.get()
        self.data = self.original_data.copy() 
        self.draw_data(self.data)
        if algo_name == "Bubble Sort":
            self.animate_bubble_sort()
        elif algo_name == "Selection Sort":
            self.animate_selection_sort()
        elif algo_name == "Fusion Sort":
            self.animate_fusion_sort()
        elif algo_name == "Heap Sort":
            self.animate_heapsort()
        elif algo_name == "Fast Sort":
            self.animate_fast_sort()
        elif algo_name == "Insertion Sort":
            self.animate_insertion_sort()
        elif algo_name == "Comb Sort":
            self.animate_comb_sort()

    def animate_bubble_sort(self):
        self.time_label.config(text=f"Time to sorted : 0.000000 s")

        print("\nBubble Sort launched...")
        print(f"Initial list : {self.data}")

        start = time.perf_counter()

        n = len(self.data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    self.draw_data(self.data, color=COLOR_ONE)
                    time.sleep(0.01)

        end = time.perf_counter()
        elapsed = end - start

        print(f"List Sorted : {self.data}")
        print(f"Time to sorted : {elapsed:.6f} secondes")


        self.time_label.config(text=f"Time to sorted : {elapsed:.6f} s")
        save_history("Bubble Sort", self.data, elapsed)
        self.execution_times["Bubble Sort"] = elapsed

    def animate_selection_sort(self):
        self.time_label.config(text=f"Time to sorted : 0.000000 s")

        print("\nSelection Sort launched...")
        print(f"Initial list : {self.data}")

        start = time.perf_counter()

        n = len(self.data)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.data[j] < self.data[min_index]:
                    min_index = j
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]
            self.draw_data(self.data, color=COLOR_TWO)
            time.sleep(0.01)

        end = time.perf_counter()
        elapsed = end - start

        print(f"List Sorted : {self.data}")
        print(f"Time to sorted : {elapsed:.6f} secondes")

        self.time_label.config(text=f"Time to sorted : {elapsed:.6f} s")
        save_history("Selection Sort", self.data, elapsed)
        self.execution_times["Selection Sort"] = elapsed

    def animate_insertion_sort(self):
        self.time_label.config(text=f"Time to sorted : 0.000000 s")

        print("\nInsertion Sort launched...")
        print(f"Initial list : {self.data}")

        start = time.perf_counter()

        n = len(self.data)
        for i in range(1,n):
            key = self.data[i]
            j = i - 1
            while j >= 0 and self.data[j] > key:
                self.data[j+1] = self.data[j]
                j = j - 1
            self.data[j+1] = key
            self.draw_data(self.data, color=COLOR_THREE)
            time.sleep(0.01)

        end = time.perf_counter()
        elapsed = end - start

        print(f"List Sorted : {self.data}")
        print(f"Time to sorted : {elapsed:.6f} secondes")

        self.time_label.config(text=f"Time to sorted : {elapsed:.6f} s")
        save_history("Insertion Sort", self.data, elapsed)
        self.execution_times["Insertion Sort"] = elapsed

    def animate_fast_sort(self):
        self.time_label.config(text=f"Time to sorted : 0.000000 s")

        print("\nFast Sort launched...")
        print(f"Initial list : {self.data}")

        start = time.perf_counter()
        bot = 0
        top = len(self.data) - 1
        fast(self.data,bot,top)
        self.draw_data(self.data, color=COLOR_FOUR)
        time.sleep(0.01)

        end = time.perf_counter()
        elapsed = end - start

        print(f"List Sorted : {self.data}")
        print(f"Time to sorted : {elapsed:.6f} secondes")

        self.time_label.config(text=f"Time to sorted : {elapsed:.6f} s")
        save_history("Quick Sort", self.data, elapsed)
        self.execution_times["Quick Sort"] = elapsed

    
    def animate_comb_sort(self):
        self.time_label.config(text=f"Time to sorted : 0.000000 s")

        print("\nComb Sort launched...")
        print(f"Initial list : {self.data}")

        start = time.perf_counter()

        n = len(self.data)
        gap = n
        shrink = 1.3
        swapped = True

        while gap > 1 or swapped:
            gap = int(gap / shrink)
            if gap < 1:
                gap = 1

            swapped = False

            for i in range(n - gap):
                if self.data[i] > self.data[i + gap]:
                    self.data[i], self.data[i + gap] = self.data[i + gap], self.data[i]
                    swapped = True
                    self.draw_data(self.data, color=COLOR_FIVE)
                    time.sleep(0.01)

        end = time.perf_counter()
        elapsed = end - start

        print(f"List Sorted : {self.data}")
        print(f"Time to sorted : {elapsed:.6f} seconds")

        self.time_label.config(text=f"Time to sorted : {elapsed:.6f} s")
        save_history("Comb Sort", self.data, elapsed)
        self.execution_times["Comb Sort"] = elapsed

    def animate_fusion_sort(self):
        self.time_label.config(text=f"Time to sorted : 0.000000 s")

        print("\nFusion Sort launched...")
        print(f"Initial list : {self.data}")

        start = time.perf_counter()

        self.data = fusion_sort(self.data, draw_callback=self.draw_data, delay=0.01)

        end = time.perf_counter()
        elapsed = end - start

        print(f"List Sorted : {self.data}")
        print(f"Time to sorted : {elapsed:.6f} secondes")

        self.time_label.config(text=f"Time to sorted : {elapsed:.6f} s")
        save_history("Fusion Sort", self.data, elapsed)
        self.execution_times["Fusion Sort"] = elapsed

    def animate_heapsort(self):
        self.time_label.config(text=f"Time to sorted : 0.000000 s")

        print("\nHeap Sort launched...")
        print(f"Initial list : {self.data}")

        start = time.perf_counter()

        self.data = heapsort_sort(self.data, draw_callback=self.draw_data, delay=0.01)

        end = time.perf_counter()
        elapsed = end - start

        print(f"List Sorted : {self.data}")
        print(f"Time to sorted : {elapsed:.6f} secondes")

        self.time_label.config(text=f"Time to sorted : {elapsed:.6f} s")
        save_history("Heap Sort", self.data, elapsed)
        self.execution_times["Heap Sort"] = elapsed


    def show_history(self):  
        try:
            with open("source/graphical/history.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        history_window = tk.Toplevel(self.root)
        history_window.title("History of sorting algorithms")
        history_window.geometry(SIZE_WINDOW)

        text_widget = tk.Text(history_window, wrap=tk.WORD)
        text_widget.pack(expand=True, fill=tk.BOTH)

        scrollbar = tk.Scrollbar(text_widget)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_widget.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text_widget.yview)

        if not data:
            text_widget.insert(tk.END, "Any sorting history found.")
        else:
            for i, entry in enumerate(data[::-1], 1):
                text_widget.insert(tk.END,
                    f"{i}. {entry['timestamp']} - {entry['algo']}\n"
                    f"   Results : {entry['result']}\n"
                    f"   Time : {entry['time']} s\n\n"
                )
    def plot_execution_times(self):
        if not self.execution_times:
            print("Any time recorded yet.")
            return

        algos = list(self.execution_times.keys())
        times = list(self.execution_times.values())

        plt.figure(figsize=(12, 6))
        plt.bar(algos, times)
        plt.ylabel("Time (seconds)")
        plt.title("Compare times of sorting algorithms")
        plt.tight_layout()
        plt.show()

def launch_visualizer():
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()

def save_history(algo_name, sorted_list, exec_time):
    history_entry = {
        "algo": algo_name,
        "result": sorted_list,
        "time": round(exec_time, 6),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        with open("source/graphical/history.json", "r", encoding="utf-8") as f:
            data = json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):
        data = []
        print("Error reading history file. Creating a new one.")

    data.append(history_entry)

    with open("source/graphical/history.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)