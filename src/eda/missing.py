import sys
import pandas as pd

pd.set_option('display.max_columns', None)

csv_path = sys.argv[1]

df = pd.read_csv(csv_path)
print(df.describe())