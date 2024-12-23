### Mô phỏng nhiệt độ
import numpy as np
temp = np.random.uniform(10.0,30.0,size=30)
round_temp = np.round(temp,2)
print(round_temp, "là ngẫu nhiên nhiệt độ trong tháng đã làm tròn 2 số sau dấu phẩy")

mean_temp = np.mean(round_temp)
print(mean_temp, "là nhiệt độ trung bình trong tháng")

### phân tích xu hướng nhiệt độ
# ý 1
max_temp = np.max(round_temp)
max_day = np.argmax(round_temp) +1    # index bắt đầu từ số 0
min_temp = np.min(round_temp)
min_day = np.argmin(round_temp) +1
print(f"Nhiệt độ cao nhất là {max_temp}, ngày nhiệt độ cao nhất là {max_day}")
print(f"Nhiệt độ thấp nhất là {min_temp}, ngày nhiệt độ thấp nhất là {min_day}")

# ý 2: thống kê sự chênh lệch nhiệt độ giữa các ngày, tìm ngày biến đổi nhiệt max
diff_temp = np.diff(round_temp)
max_diff = np.argmax(diff_temp) + 1
print(diff_temp, "là chênh lệch nhiệt độ giữa các ngày")
print("ngày biến đổi nhiệt độ lớn nhất là:", max_diff)

### áp dụng fancy index
higher_than_20 = round_temp[round_temp >20]
indices = [4,9,14,19,24]    # index bắt đầu từ 0
temp_of_specified_day = round_temp[indices]
mean_temp = np.mean(round_temp)
higher_than_mean = round_temp[round_temp >mean_temp]
odd_temp = round_temp[::2]
even_temp = round_temp[1::2]
print(higher_than_20, "là các ngày >20 độ")
print(temp_of_specified_day, "là nhiệt độ các ngày 5-10-15-20-25")
print(higher_than_mean, "là nhiệt độ các ngày trên trung bình")
print(odd_temp, "là nhiệt độ ngày lẻ")
print(even_temp, "là nhiệt độ ngày chẵn")
