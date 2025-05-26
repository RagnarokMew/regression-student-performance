import sys
import pandas as pd

pd.set_option('display.max_columns', None) # so i can ctrl + c the output to the pdf

##################
## Load dataset ##
##################

csv_path = sys.argv[1]

df = pd.read_csv(csv_path)

print()


#########################################################
## Calculating number and percentage of missing values ##
#########################################################

for val in df:
    missing = df[val].isnull().sum()
    print(f"{val}: {missing} / {round(missing / len(df) * 100, 2)}% missing values")

print()

print(df.describe())