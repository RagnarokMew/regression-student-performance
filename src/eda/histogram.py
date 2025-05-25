import sys
import pandas as pd
import matplotlib.pyplot as plt

csv_path = sys.argv[1]

df = pd.read_csv(csv_path)

numeric_cols = df.select_dtypes(include='number')

print(numeric_cols.columns.tolist())