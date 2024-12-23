import numpy as np
import pandas as pd
# ý 1
df = pd.read_csv("D:/17A3KHDL/LAB2/DATA/diem_hoc_phan.csv")

print("5 dòng đầu tiên là :")
print(df.head())

data_list = df.values.tolist()

data_numpy = np.array(data_list)

print("Dữ liệu dưới dạng list là :", data_list)
print("Dữ liệu dưới dạng numpy là :", data_numpy)

data_array = np.array(data_list)
print(data_array)

# ý 2
cot_diem = data_array[:,2:].astype(float)

def diem_tin_chi(diem):
        if 8.5 <= diem <= 10 :
            return 'A'
        elif 8.0 <= diem <= 8.4:
            return 'B+'
        elif 7.0 <= diem < 8.0:
            return 'B'
        elif 6.5 <= diem < 7.0:
            return 'C+'
        elif 5.5 <= diem < 6.0:
            return 'C'
        elif 5.0 <= diem < 5.5:
            return 'D+'
        elif 4.0 <= diem < 5.0:
            return 'D'
        else :
            return 'F'
        
quy_doi_diem = np.vectorize(diem_tin_chi)(cot_diem)
print("diem tin chi la: ", quy_doi_diem)

# ý 3
hp1 = quy_doi_diem[:,0]
hp2 = quy_doi_diem[:,1]
hp3 = quy_doi_diem[:,2]

print("Điểm học phần 1 là :", hp1)
print("Điểm học phần 2 là :", hp2)
print("Điểm học phần 3 là :", hp3)

# ý 4
total_hp1 = df['HP 1'].sum()
total_hp2 = df['HP 2'].sum()
total_hp3 = df['HP 3'].sum()

mean_hp1 = df['HP 1'].mean()
mean_hp2 = df['HP 2'].mean()
mean_hp3 = df['HP 3'].mean()

std_hp1 = df['HP 1'].std()
std_hp2 = df['HP 2'].std()
std_hp3 = df['HP 3'].std()

print("Tổng điểm học phần 1 là :", total_hp1, "Trung bình là :", mean_hp1, "độ lệch chuẩn là :", std_hp1)
print("Tổng điểm học phần 2 là :", total_hp2, "Trung bình là :", mean_hp2, "độ lệch chuẩn là :", std_hp2)
print("Tổng điểm học phần 3 là :", total_hp3, "Trung bình là :", mean_hp3, "độ lệch chuẩn là :", std_hp3)

# ý 5
unique, count = np.unique(quy_doi_diem,return_counts=True)
so_luong_diem_chu = dict(zip(unique,count))
print("\nSố lượng sinh viên đạt từng loại điểm chữ\n",so_luong_diem_chu)
