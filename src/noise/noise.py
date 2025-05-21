import numpy as np
import pandas as pd

##############################
## Loading original dataset ##
##############################

df = pd.read_csv("../../data/original_student_habits_performance.csv")

print(df.info())

######################################
## Creating masks for removing data ##
######################################

mask_study_hours = np.random.rand(len(df)) < 0.05
mask_extra_activity = np.random.rand(len(df)) < 0.2
mask_diet_quality = np.random.rand(len(df)) < 0.1
mask_mental_health = np.random.rand(len(df)) < 0.01
mask_age = np.random.rand(len(df)) < 0.01
mask_social_media = np.random.rand(len(df)) < 0.1
mask_netflix = np.random.rand(len(df)) < 0.25

df.loc[mask_study_hours, 'study_hours_per_day'] = np.nan
df.loc[mask_age, 'age'] = np.nan
df.loc[mask_diet_quality, 'diet_quality'] = np.nan
df.loc[mask_extra_activity, 'extracurricular_participation'] = np.nan
df.loc[mask_social_media, 'social_media_hours'] = np.nan
df.loc[mask_mental_health, 'mental_health_rating'] = np.nan
df.loc[mask_netflix, 'netflix_hours'] = np.nan

print(df.info())