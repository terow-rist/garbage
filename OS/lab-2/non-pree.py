totalprocess = 5

proc = [[0 for _ in range(4)] for _ in range(totalprocess)]

def get_wt_time(wt):
    service = [0] * totalprocess
    service[0] = 0
    wt[0] = 0
    for i in range(1, totalprocess):
        service[i] = proc[i - 1][1] + service[i - 1]
        wt[i] = service[i] - proc[i][0] + 1
        if wt[i] < 0:
            wt[i] = 0

def get_tat_time(tat, wt):
    for i in range(totalprocess):
        tat[i] = proc[i][1] + wt[i]

def findgc():
    wt = [0] * totalprocess
    tat = [0] * totalprocess
    wavg = 0
    tavg = 0

    get_wt_time(wt)
    get_tat_time(tat, wt)

    stime = [0] * totalprocess
    ctime = [0] * totalprocess

    stime[0] = 1
    ctime[0] = stime[0] + tat[0]

    for i in range(1, totalprocess):
        stime[i] = ctime[i - 1]
        ctime[i] = stime[i] + tat[i] - wt[i]

    print("Process_no\tStart_time\tComplete_time\tTurn_Around_Time\tWaiting_Time")
    for i in range(totalprocess):
        wavg += wt[i]
        tavg += tat[i]
        print(
            f"{proc[i][3]}\t\t{stime[i]}\t\t{ctime[i]}\t\t{tat[i]}\t\t\t{wt[i]}"
        )

    print(f"Average waiting time is : {wavg / totalprocess}")
    print(f"Average turnaround time : {tavg / totalprocess}")

arrivaltime = [1, 2, 3, 4, 5]
bursttime = [3, 5, 1, 7, 4]
priority = [3, 4, 1, 7, 8]

for i in range(totalprocess):
    proc[i][0] = arrivaltime[i]
    proc[i][1] = bursttime[i]
    proc[i][2] = priority[i]
    proc[i][3] = i + 1

proc.sort(key=lambda x: (x[2], x[0]))

findgc()
