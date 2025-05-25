import sys
import pandas as pd
import matplotlib.pyplot as plt

csv_path = sys.argv[1]
df = pd.read_csv(csv_path)

numeric = df.select_dtypes(include='number')

for feature in numeric:
    q25th = df[feature].quantile(0.25)
    q75th = df[feature].quantile(0.75)
    iqr = q75th - q25th

    outliers = df[(df[feature] < q25th - 1.5 * iqr) | (df[feature] > q75th + 1.5 * iqr)][feature]
    print(f"{feature} outlier count: {outliers.count()}")
    plt.title(f"Outlier boxplot {feature}")
    plt.boxplot(df[feature])
    plt.savefig(f"../../raw/outlier_{feature}.png")
    plt.close