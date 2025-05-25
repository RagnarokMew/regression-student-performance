import sys
import numpy as np
import pandas as pd

csv_path = sys.argv[1]
df = pd.read_csv(csv_path)

df['age'].fillnas(df['age'].median(), inplace=True)
df['study_hours_per_day'].fillnas(df['study_hours_per_day'].median(), inplace=True)
df['social_media_hours'].fillnas(df['social_media_hours'].median(), inplace=True)
df['netflix_hours'].fillnas(df['netflix_hours'].median(), inplace=True)

df['diet_quality']
df['parental_education_level']
df['mental_health_rating']
df['extracurricular_participation']

df.to_csv(f"../../data/final.csv", index=False)