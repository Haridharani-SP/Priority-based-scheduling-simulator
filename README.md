# Priority based scheduling simulator
Priority-Based Task Scheduling Simulator
Overview

This project is a terminal-based simulation of task scheduling strategies.
It compares how different scheduling algorithms decide which task should be executed first when only one resource is available at a time.

The project is inspired by real-world decision-making scenarios, especially IT helpdesk operations, where multiple tasks (tickets) arrive over time with different priorities and deadlines.

The main goal of this simulator is to understand how scheduling policies affect performance metrics such as waiting time, turnaround time, and SLA violations.

Task Explanation

In many systems, tasks do not arrive all at once. They come at different times, require different amounts of processing time, and may have different levels of importance.

Since only one task can be executed at a time, the system must decide:
Which task should be processed next?

This project simulates that decision using multiple scheduling strategies and compares their performance.

Input

Each task has the following attributes:

Task ID – Unique identifier for the task

Arrival Time – Time at which the task enters the system

Execution Time – Time required to complete the task

Priority – Importance of the task (lower value = higher priority)

Deadline – Time before which the task should be completed to avoid SLA violation

The input data is stored in a JSON file (tickets.json).

Scheduling Strategies Implemented

The simulator compares the following algorithms:

1. First Come First Serve (FCFS)

Tasks are executed in the order they arrive

Very simple to implement

Can cause long delays if an early task takes a lot of time

2. Shortest Job First (SJF)

Task with the shortest execution time is selected

Improves overall efficiency

Does not consider task urgency or deadlines

3. Priority Scheduling

Tasks with higher priority are executed first

Better suited for systems with SLAs

Low-priority tasks may wait longer

Output Metrics

For each scheduling strategy, the simulator prints the following in the terminal:

Execution order of tasks

Start time and finish time of each task

Average waiting time

Average turnaround time

Number of SLA violations

This makes it easy to compare how each strategy behaves under the same workload.

Use Case Explanation: IT Helpdesk Ticket Scheduling
Background

In most organizations, the IT helpdesk receives multiple support tickets throughout the day.
These tickets may involve issues such as system failures, login problems, payment errors, or feature requests.

However, the number of support engineers is limited. In many cases, only one engineer (or one active processing slot) is available at a time.

This creates a real decision-making problem:
Which ticket should be resolved first?

Mapping the Use Case to the Simulator

In this project, each helpdesk ticket is treated as a task:

Ticket Concept	Simulator Attribute
Ticket raised time	Arrival Time
Time to fix issue	Execution Time
Severity (P1, P2, P3)	Priority
SLA deadline	Deadline

The support engineer is modeled as a single resource that can process only one ticket at a time.

Why Scheduling Matters in This Use Case

If tickets are handled without a clear policy:

Critical issues may get delayed

SLAs may be violated

User satisfaction may decrease

Business impact may increase

Different scheduling strategies lead to different outcomes, which is why comparing them is important.

Best Strategy for This Use Case

Based on the simulation results, Priority Scheduling performs best for the IT helpdesk scenario.

Reasoning:

Business-critical tickets are handled first

SLA violations for high-priority issues are reduced

The approach matches real-world helpdesk workflows

Higher waiting time for low-priority tickets is an acceptable trade-off

This shows that in SLA-driven systems, urgency is more important than fairness or raw efficiency.

Decision-Making Perspective

This project models a real-world decision-making problem under constraints:

Resources are limited

Tasks have different importance

Multiple performance metrics must be balanced

The simulator provides a quantitative way to evaluate decisions and choose a strategy that aligns with business goals.
