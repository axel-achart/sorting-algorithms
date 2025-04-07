# source/graphical/graphical.py

import tkinter as tk
import random
import time
import json
from datetime import datetime
import matplotlib.pyplot as plt
from source.algos.selection_sort import selection_sort
from source.algos.bubble_sort import bubble_sort

# Dictionnaire pour sélectionner dynamiquement le tri
algorithms = {
    "Tri à bulles": bubble_sort,
    "Tri par sélection": selection_sort
}

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualisation des algorithmes de tri")
        self.canvas = tk.Canvas(root, width=800, height=400, bg="white")
        self.canvas.pack(padx=10, pady=10)
        self.execution_times = {}
        
       # Contrôles
        control_frame = tk.Frame(root)
        control_frame.pack()

        self.algo_var = tk.StringVar(value="Tri à bulles")
        tk.OptionMenu(control_frame, self.algo_var, *algorithms.keys()).pack(side=tk.LEFT, padx=5)

        tk.Button(control_frame, text="Nouvelle liste", command=self.generate_data).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Lancer le tri", command=self.run_sort).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Voir l’historique", command=self.show_history).pack(side=tk.LEFT)
        tk.Button(control_frame, text="Comparer les temps", command=self.plot_execution_times).pack(side=tk.LEFT, padx=5)

        # Label pour afficher le temps
        self.time_label = tk.Label(root, text="Temps d'exécution : 0.000000 s", font=("Arial", 12))
        self.time_label.pack(pady=5)

        # Taille de la liste (entre 10 et 100)
        self.list_size = tk.IntVar(value=50)
        tk.Label(control_frame, text="Taille de la liste").pack(side=tk.LEFT, padx=5)
        tk.Scale(control_frame, from_=10, to=100, orient=tk.HORIZONTAL, variable=self.list_size).pack(side=tk.LEFT, padx=5)


        self.generate_data()

    def generate_data(self):
        size = self.list_size.get()
        self.original_data = [random.randint(10, 390) for _ in range(size)]
        self.data = self.original_data.copy()
        self.draw_data(self.data)


    def draw_data(self, data, color="blue"):
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
        self.data = self.original_data.copy()  # ⬅️ On repart toujours de la même liste
        self.draw_data(self.data)
        if algo_name == "Tri à bulles":
            self.animate_bubble_sort()
        elif algo_name == "Tri par sélection":
            self.animate_selection_sort()

    def animate_bubble_sort(self):
        print("\n🔁 Tri à bulles lancé...")
        print(f"Liste initiale : {self.data}")

        start = time.perf_counter()

        n = len(self.data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    self.draw_data(self.data, color="orange")
                    time.sleep(0.01)

        end = time.perf_counter()
        elapsed = end - start

        print(f"✅ Liste triée : {self.data}")
        print(f"⏱️ Temps d'exécution : {elapsed:.6f} secondes")


        self.time_label.config(text=f"Temps d'exécution : {elapsed:.6f} s")
        save_history("Tri à bulles", self.data, elapsed)
        self.execution_times["Tri à bulles"] = elapsed


    def animate_selection_sort(self):
        print("\n🔁 Tri par sélection lancé...")
        print(f"Liste initiale : {self.data}")

        start = time.perf_counter()

        n = len(self.data)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.data[j] < self.data[min_index]:
                    min_index = j
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]
            self.draw_data(self.data, color="purple")
            time.sleep(0.01)

        end = time.perf_counter()
        elapsed = end - start

        print(f"✅ Liste triée : {self.data}")
        print(f"⏱️ Temps d'exécution : {elapsed:.6f} secondes")

        self.time_label.config(text=f"Temps d'exécution : {elapsed:.6f} s")
        save_history("Tri par sélection", self.data, elapsed)
        self.execution_times["Tri par sélection"] = elapsed
    
    def show_history(self):  
        try:
            with open("source/graphical/history.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        history_window = tk.Toplevel(self.root)
        history_window.title("Historique des tris")
        history_window.geometry("600x400")

        text_widget = tk.Text(history_window, wrap=tk.WORD)
        text_widget.pack(expand=True, fill=tk.BOTH)

        scrollbar = tk.Scrollbar(text_widget)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_widget.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text_widget.yview)

        if not data:
            text_widget.insert(tk.END, "Aucun tri enregistré pour le moment.")
        else:
            for i, entry in enumerate(data[::-1], 1):
                text_widget.insert(tk.END,
                    f"{i}. {entry['timestamp']} - {entry['algo']}\n"
                    f"   Résultat : {entry['result']}\n"
                    f"   Temps : {entry['time']} s\n\n"
                )
    def plot_execution_times(self):
        if not self.execution_times:
            print("Aucun temps d'exécution enregistré.")
            return

        algos = list(self.execution_times.keys())
        times = list(self.execution_times.values())

        plt.figure(figsize=(6, 4))
        plt.bar(algos, times)
        plt.ylabel("Temps (secondes)")
        plt.title("Comparaison des temps d'exécution")
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

    data.append(history_entry)

    with open("source/graphical/history.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
