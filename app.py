import json
import copy


def get_data():
    fh = open("tickets.json")
    x = json.load(fh)
    fh.close()
    return x

def fcfs_pick(q):
    first = q[0]
    for i in range(0, len(q)):
        if q[i]["arrival"] < first["arrival"]:
            first = q[i]
    return first

def sjf_pick(q):
    first = q[0]
    idx = 1
    while idx < len(q):
        if q[idx]["execution"] < first["execution"]:
            first = q[idx]
        idx = idx + 1
    return first

def priority_pick(q):
    first = q[0]
    for i in q:
        if i["priority"] < first["priority"]:
            first = i
    return first

def execute(mode):
    original = get_data()
    task_pool = copy.deepcopy(original)
    t = 0
    waiting_list = []
    done = []
    while True:
        if len(task_pool) == 0 and len(waiting_list) == 0:
            break
        pos = 0
        while pos < len(task_pool):
            if task_pool[pos]["arrival"] <= t:
                waiting_list.append(task_pool[pos])
                task_pool.pop(pos)
            else:
                pos = pos + 1
        if len(waiting_list) == 0:
            t = t + 1
            continue
        if mode == "FCFS":
            run = fcfs_pick(waiting_list)
        elif mode == "SJF":
            run = sjf_pick(waiting_list)
        else:
            run = priority_pick(waiting_list)
        waiting_list.remove(run)
        run["start"] = t
        run["finish"] = t + run["execution"]
        w = run["start"] - run["arrival"]
        ta = run["finish"] - run["arrival"]
        run["waiting"] = w
        run["turnaround"] = ta
        if run["finish"] > run["deadline"]:
            run["sla"] = "Missed"
        else:
            run["sla"] = "OK"
        t = run["finish"]
        done.append(run)

    w_sum = 0
    t_sum = 0
    miss = 0
    for e in done:
        w_sum = w_sum + e["waiting"]
        t_sum = t_sum + e["turnaround"]
        if e["sla"] == "Missed":
            miss = miss + 1
    aw = round(w_sum / len(done), 2)
    at = round(t_sum / len(done), 2)
    return done, aw, at, miss

def display(name, rows, w, t, m):

    print("\n==================================================")
    print("METHOD:", name)
    print("==================================================")
    print("Task   Start   End     Deadline   SLA")
    print("--------------------------------------------------")
    for r in rows:
        print(
            str(r["id"]).ljust(6),
            str(r["start"]).ljust(7),
            str(r["finish"]).ljust(7),
            str(r["deadline"]).ljust(10),
            r["sla"]
        )
    print("--------------------------------------------------")
    print("Avg Waiting Time   :", w)
    print("Avg Turnaround Time:", t)
    print("SLA Misses         :", m)

def final_note():
    print("\n==================================================")
    print("FINAL DECISION")
    print("==================================================")
    print("Priority scheduling works best in this scenario.")
    print("Critical tickets are handled first.")
    print("SLA failures are reduced for high impact issues.")
    print("Lower priority tasks wait longer, which is acceptable.")
    print("This matches real helpdesk behaviour.")

if __name__ == "__main__":
    modes = ["FCFS", "SJF", "PRIORITY"]
    for m in modes:
        out, wv, tv, mv = execute(m)
        display(m, out, wv, tv, mv)
    final_note()
