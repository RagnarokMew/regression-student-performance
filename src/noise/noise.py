import numpy as np
import pandas as pd

##############################
## Loading original dataset ##
##############################

df = pd.read_csv("../../data/original_student_habits_performance.csv")

print(df.info())

##################################
## Introducing noise to dataset ##
##################################

noise_attendance = np.random.normal(-10, 10, size=len(df))
noise_sleep = np.random.normal(0.9, 1.1, size=len(df))
noise_mental_health = np.random.randint(-1, 2, size=len(df))
noise_exercise_freq = np.random.randint(-1, 2, size=len(df))

df['attendance_percentage'] += noise_attendance
df['sleep_hours'] *= noise_sleep
df['mental_health_rating'] += noise_mental_health
df['exercise_frequency'] += noise_exercise_freq

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