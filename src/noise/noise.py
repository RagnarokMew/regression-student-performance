import numpy as np
import pandas as pd

df = pd.read_csv("../../data/original_student_habits_performance.csv")

print(df.info())

mask_study_hours = np.random.rand(len(df)) < 0.05
mask_extre_activity = np.random.rand(len(df)) < 0.2
mask_diet_quality = np.random.rand(len(df)) < 0.1
mask_mental_health = np.random.rand(len(df)) < 0.01
mask_age = np.random.rand(len(df)) < 0.01
mask_sociaL_media = np.random.rand(len(df)) < 0.1