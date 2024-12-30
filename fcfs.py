at = []
pid = []
bt = [] 
wt = []
ct  = []
tat = []
n = int(input("Enter no of Processes: "))
for i in range(0,n):
    ele = int(input("Enter the arrivial time for process {0}: ".format(i)))
    at.append(ele)
    ele = int(input("Enter the burst time for process {0}: ".format(i)))
    bt.append(ele)
    pid.append(i)

for j in range(0,n):
    if j == 0:
        value = bt[j]
        ct.append(value)
    else:
        value= ct[j - 1] + bt[j]
        ct.append(value)
    #value = ct[j] - at [j]
    tat.append(ct[j] - at [j])
    wt.append(tat [j] - bt[j])
    
for k in range(0,n):
    print(pid[k], end =" ")
    print(at[k], end =" ")
    print(bt[k], end =" ")
    print(ct[k], end =" ")
    print(tat[k], end =" ")
    print(wt[k])