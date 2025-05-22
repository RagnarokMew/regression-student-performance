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

#############################
## Ensure bounds of values ##
#############################

df.loc[df['attendance_percentage'] > 100, 'attendance_percentage'] = 100.00
df.loc[df['attendance_percentage'] < 0, 'attendance_percentage'] = 0.00

df.loc[df['sleep_hours'] > 24, 'sleep_hours'] = 24.00
df.loc[df['sleep_hours'] < 0, 'sleep_hours'] = 0.00

df.loc[df['mental_health_rating'] > 10, 'mental_health_rating'] = 10
df.loc[df['mental_health_rating'] < 0, 'mental_health_rating'] = 0

df.loc[df['exercise_frequency'] > 7, 'exercise_frequency'] = 7
df.loc[df['exercise_frequency'] < 0, 'exercise_frequency'] = 0

######################################
## Creating masks for removing data ##
######################################

mask_study_hours = np.random.rand(len(df)) < 0.05
mask_extra_activity = np.random.rand(len(df)) < 0.2
mask_diet_quality = np.random.rand(len(df)) < 0.1
mask_mental_health = np.random.rand(len(df)) < 0.15
mask_age = np.random.rand(len(df)) < 0.05
mask_social_media = np.random.rand(len(df)) < 0.1
mask_netflix = np.random.rand(len(df)) < 0.25

df.loc[mask_study_hours, 'study_hours_per_day'] = np.nan
df.loc[mask_age, 'age'] = np.nan
df.loc[mask_diet_quality, 'diet_quality'] = np.nan
df.loc[mask_extra_activity, 'extracurricular_participation'] = np.nan
df.loc[mask_social_media, 'social_media_hours'] = np.nan
df.loc[mask_mental_health, 'mental_health_rating'] = np.nan
df.loc[mask_netflix, 'netflix_hours'] = np.nan

###########################################
## Change types to handle missing values ##
##   to preserve original column types   ##
###########################################

df['age'] = df['age'].astype('Int64')
df['mental_health_rating'] = df['mental_health_rating'].astype('Int64')

print(df.info())
df.to_csv("../../data/noised_student_habits_performance.csv", index=False)