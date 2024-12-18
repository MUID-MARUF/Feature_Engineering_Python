import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset (replace with your own dataset)
# Example: Load a CSV file
data = pd.read_csv("your_dataset.csv")

# Calculate the correlation matrix
correlation_matrix = data.corr()

# Print the correlation matrix
print(correlation_matrix)

# Visualize the correlation matrix with a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.show()
