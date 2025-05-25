import sys
import numpy as np
import pandas as pd

csv_path = sys.argv[1]
df = pd.read_csv(csv_path)

df['gender'] = df['gender'].map({
    'Male': 0,
    'Female': 1,
    'Other': 2
})
df['part_time_job'] = df['part_time_job'].map({
    'Yes': 1,
    'No': 0
})
df['diet_quality'] = df['diet_quality'].map({
    'Poor': 0,
    'Fair': 1,
    'Good': 2
})
df['parental_education_level'] = df['parental_education_level'].map({
    None: 0,
    'High School': 1,
    'Bachelor': 2,
    'Master': 3,
})
df['internet_quality'] = df['internet_quality'].map({
    'Poor': 0,
    'Average': 1,
    'Good': 2
})
df['extracurricular_participation'] = df['extracurricular_participation'].map({
    'Yes': 1,
    'No': 0
})

df.to_csv(f"../../data/processed.csv", index=False)