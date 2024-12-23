# ý 1
import numpy as np
efficiency = []
with open('D:/17A3KHDL/LAB2/DATA/efficiency.txt','r',encoding='utf-8') as file:
    for line in file:
        efficiency.append(float(line.strip()))
        print(efficiency)

shifts = []
with open("D:/17A3KHDL/LAB2/DATA/shifts.txt",'r',encoding='utf-8') as f:
    for line in f:
        shifts.append(line.strip())
        print(shifts)

# ý 2
np_shifts = np.array(shifts,dtype=str)
print(np_shifts.dtype)

# ý 3
np_efficiency = np.array(efficiency,dtype=float)
print(np_efficiency.dtype)

# ý 4
morning_mean_eff = np_efficiency[np_shifts == "Morning"]
print(np.mean(morning_mean_eff), "là hiệu suất trung bình ca sáng")

# ý 5
another_shifts_mean_eff = np_efficiency[np_shifts != "Morning"]
print(np.mean(another_shifts_mean_eff), "là hiệu suất trung bình các ca còn lại")

# ý 6
structure = np.dtype([('shift','U10'),('efficiency','float')])
workers = np.array(list(zip(shifts,efficiency)),dtype=structure)

# ý 7
sorted_workers = np.sort(workers,order='efficiency')
max_eff = sorted_workers[-1]['shift']    
min_eff = sorted_workers[0]['shift']
print(max_eff,min_eff)