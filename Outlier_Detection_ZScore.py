import numpy as np
outliers = []
def detect_outliers_zscore(data):
thres = 3
mean = np.mean(data)
std = np.std(data)
# print(mean, std)
for i in data:
z_score = (i-mean)/std
if (np.abs(z_score) > thres):
outliers.append(i)
return outliers# Driver code
sample_outliers = detect_outliers_zscore(sample)
print("Outliers from Z-scores method: ", sample_outliers)
