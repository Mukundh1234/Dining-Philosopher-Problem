import tkinter as tk
from tkinter import ttk
import heapq

class Process:
    def __init__(self, name, priority, burst_time):
        self.name = name
        self.priority = priority
        self.burst_time = burst_time

process_queue = []

def add_process():
    name = name_entry.get()
    priority = int(priority_entry.get())
    burst_time = int(burst_time_entry.get())
    process = Process(name, priority, burst_time)
    heapq.heappush(process_queue, (priority, process))
    update_display()

def run_scheduler():
    result_text.delete(1.0, tk.END)
    while process_queue:
        priority, process = heapq.heappop(process_queue)
        result_text.insert(tk.END, f"Running {process.name}...  ")
        process.burst_time -= 1
        if process.burst_time > 0:
            heapq.heappush(process_queue, (process.priority, process))
        update_display()

def update_display():
    process_listbox.delete(0, tk.END)
    for _, process in process_queue:
        process_listbox.insert(tk.END, f"{process.name} (Priority: {process.priority}, Burst Time: {process.burst_time})")

window = tk.Tk()
window.title("Priority Scheduling Simulation")
window.geometry("800x600")
window.configure(bg="#E0E0E0")

header_label = tk.Label(window, text="Priority Scheduling Simulation", font=("Helvetica", 20, "bold"), bg="#1E90FF", fg="white")
header_label.pack(fill="x", padx=20, pady=10)

input_frame = tk.Frame(window, bg="#E0E0E0")
input_frame.pack(padx=20, pady=10, fill="both")


style = ttk.Style()
style.configure("TLabel", background="#E0E0E0")
style.configure("TEntry", fieldbackground="lightgrey")
style.configure("TButton", background="#32CD32", padding=10)

name_label = ttk.Label(input_frame, text="Process Name", font=("Helvetica", 14), padding=10)
name_label.grid(row=0, column=0, padx=10)
name_entry = ttk.Entry(input_frame)
name_entry.grid(row=0, column=1, padx=10)

priority_label = ttk.Label(input_frame, text="Priority", font=("Helvetica", 14), padding=10)
priority_label.grid(row=0, column=2, padx=10)
priority_entry = ttk.Entry(input_frame)
priority_entry.grid(row=0, column=3, padx=10)

burst_time_label = ttk.Label(input_frame, text="Burst Time", font=("Helvetica", 14), padding=10)
burst_time_label.grid(row=0, column=4, padx=10)
burst_time_entry = ttk.Entry(input_frame)
burst_time_entry.grid(row=0, column=5, padx=10)


add_button = ttk.Button(input_frame, text="Add Process", command=add_process)
add_button.grid(row=1, column=0, columnspan=2, pady=20)

run_button = ttk.Button(input_frame, text="Run Scheduler", command=run_scheduler, style="TButton")
run_button.grid(row=1, column=2, columnspan=2, pady=20)


process_listbox = tk.Listbox(window, bg="lightgrey", width=60, height=10, font=("Helvetica", 14))
process_listbox.pack(padx=20, pady=10)


result_label = tk.Label(window, text="Execution Log", font=("Helvetica", 16, "bold"), bg="#E0E0E0")
result_label.pack(padx=20)

result_text = tk.Text(window, height=10, width=60, bg="lightgrey", font=("Helvetica", 14))
result_text.pack(padx=20, pady=10)

window.mainloop()
