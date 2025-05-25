import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

csv_path = sys.argv[1]
df = pd.read_csv(csv_path)

numeric = df.select_dtypes(include='number')
corr_target = numeric.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(corr_target, annot=True, fmt=".2f", cmap='Blues', linewidths=0.5)
plt.title('Correlation matrix heatmap')
plt.xticks(rotation=90)
plt.tight_layout()
plt.title('Correlation matrix heatmap')
plt.savefig("../../raw/corr_heat.png")