import sys
import numpy as np
import pandas as pd

##################
## Load dataset ##
##################

csv_path = sys.argv[1]

df = pd.read_csv(csv_path)

############################
## Filling missing values ##
############################

# NOTE: I know it generates warnings when run (check pdf), but it works, it's simple and it was easy to write 

df['age'].fillna(df['age'].median(), inplace=True)
df['study_hours_per_day'].fillna(df['study_hours_per_day'].median(), inplace=True)
df['social_media_hours'].fillna(df['social_media_hours'].median(), inplace=True)
df['netflix_hours'].fillna(df['netflix_hours'].median(), inplace=True)

df['diet_quality'].fillna(df['diet_quality'].mode()[0], inplace=True)
df['parental_education_level'].fillna(df['parental_education_level'].mode()[0], inplace=True)
df['mental_health_rating'].fillna(df['mental_health_rating'].mode()[0], inplace=True)
df['extracurricular_participation'].fillna(df['extracurricular_participation'].mode()[0], inplace=True)

df.to_csv("../../data/final.csv", index=False)