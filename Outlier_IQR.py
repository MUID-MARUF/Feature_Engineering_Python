outliers = []
def detect_outliers_iqr(data):
data = sorted(data)
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
# print(q1, q3)
IQR = q3-q1
lwr_bound = q1-(1.5*IQR)
upr_bound = q3+(1.5*IQR)
# print(lwr_bound, upr_bound)
for i in data:
if (i<lwr_bound or i>upr_bound):
outliers.append(i)
return outliers# Driver code
sample_outliers = detect_outliers_iqr(sample)
print("Outliers from IQR method: ", sample_outliers)
# Trimming
sample = np.delete(sample, np.isin(sample, sample_outliers))
print(sample)
Replace outliers with Mean Value:
def replace_outliers_with_mean(data):
outliers = detect_outliers_iqr(data)
mean_value = np.mean(data)
# Replace each outlier in the data with the mean value
data = np.array(data) # Ensure data is a numpy array for easy indexing
for outlier in outliers:
data[np.where(data == outlier)] = mean_value
return data
# Sample data
sample = [10, 12, 12, 15, 100, 12, 13, 14, 18, 120]
sample_replaced = replace_outliers_with_mean(sample)
print("Data after replacing outliers with mean:", sample_replaced)
