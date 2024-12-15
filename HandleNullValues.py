import pandas as pd

#read csv file & create dataframe
data = pd.read("path_directory")

#for null value deletion:
new_data = data.dropna(inplace = False)

#for replacing the null values with 0:
new_data = data.fillna(0)


#It's better to drop/delete the null values than imputation in most of the cases.
