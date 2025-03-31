import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Generate synthetic dataset with outliers
np.random.seed(42)
data = np.random.normal(loc=50, scale=10, size=100).tolist()
data.extend([10, 120, 5, 150])  # Adding some outliers

df = pd.DataFrame({'Value': data})

# Z-Score Method for Outlier Detection
def detect_outliers_zscore(data, threshold=3):
    mean = np.mean(data)
    std = np.std(data)
    z_scores = [(x - mean) / std for x in data]
    return np.where(np.abs(z_scores) > threshold)[0]

outliers_z = detect_outliers_zscore(df['Value'])

# IQR Method for Outlier Detection
def detect_outliers_iqr(data):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return np.where((data < lower_bound) | (data > upper_bound))[0]

outliers_iqr = detect_outliers_iqr(df['Value'])

# Plot Data with Outliers
plt.figure(figsize=(10,5))
sns.boxplot(x=df['Value'])
plt.title("Box Plot for Outlier Detection")
plt.show()

# Print Outliers
print(f"Outliers detected using Z-Score: {df.iloc[outliers_z].values}")
print(f"Outliers detected using IQR: {df.iloc[outliers_iqr].values}")

# Save dataset to CSV
df.to_csv("outlier_dataset.csv", index=False)