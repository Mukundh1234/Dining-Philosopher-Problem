Overview

The Priority Scheduling Simulation is a graphical user interface (GUI) application built using Python's Tkinter library. The program simulates the priority scheduling algorithm, which is a non-preemptive scheduling algorithm in operating systems. Each process is assigned a priority, and the process with the highest priority is selected first for execution. The application allows users to add processes, specify their burst time and priority, and simulate the execution of these processes based on their priorities.


Features:

Add processes with custom names, priorities, and burst times.
Simulate the execution of processes based on their priority.
View a list of the processes and their current state (priority, burst time).
Execution log displays the current process being executed.


Requirements

Python 3.x
Tkinter (usually comes pre-installed with Python)

How to Use:

Add a Process: Enter the process name, priority, and burst time in the input fields, then click the "Add Process" button. The process will be added to the process queue.

Run Scheduler: After adding processes, click the "Run Scheduler" button to start the simulation. The processes will be executed in order of their priority, and the execution log will be updated as the processes run.

View Process List: The list of processes will display with their name, priority, and remaining burst time.


Code Explanation

Process Class: Represents a process with a name, priority, and burst time.

Priority Queue: The process_queue is implemented using a heapq (priority queue), where the process with the highest priority (lowest numeric value) is always selected first for execution.

Scheduler Logic: The run_scheduler function simulates the execution of the processes in the queue. It updates the burst time of each process and moves the process back into the queue if it still has burst time remaining.

GUI: Built using Tkinter with various widgets such as labels, buttons, and list boxes to interact with the user.
