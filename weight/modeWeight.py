from collections import Counter
import csv

with open('height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][2]
	new_data.append(n_num)

#Calculating Mode
data = Counter(new_data)
mode_data_for_range = {"100-120": 0, "120-140": 0, "140-160": 0}
for height, occurence in data.items():
    if 100 < float(height) < 120:
        mode_data_for_range["100-120"] += occurence
    elif 120 < float(height) < 140:
        mode_data_for_range["120-140"] += occurence
    elif 140 < float(height) < 160:
        mode_data_for_range["140-160"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")