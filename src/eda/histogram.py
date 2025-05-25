import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

csv_path = sys.argv[1]

df = pd.read_csv(csv_path).dropna()

##############################
## Discrete Values Plotting ##
##############################

min, max = df['age'].min(), df['age'].max()
bins = np.arange(min - 0.5, max + 0.5)

plt.hist(df['age'], bins=bins, align='mid', color='lightskyblue', edgecolor='black')
plt.title('Age ditribution of students')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.savefig("../../raw/hist_age.png")
plt.close()


min, max = df['exercise_frequency'].min(), df['exercise_frequency'].max()
bins = np.arange(min - 0.5, max + 0.5)

plt.hist(df['exercise_frequency'], bins=bins, align='mid', color='lightskyblue', edgecolor='black')
plt.title('Exercise frequency ditribution of students')
plt.xlabel('Exercise per week')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.savefig("../../raw/hist_exercise.png")
plt.close()


min, max = df['mental_health_rating'].min(), df['mental_health_rating'].max()
bins = np.arange(min - 0.5, max + 0.5)

plt.hist(df['mental_health_rating'], bins=bins, align='mid', color='lightskyblue', edgecolor='black')
plt.title('Mental health ditribution of students')
plt.xlabel('Mental health score')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.savefig("../../raw/hist_mental.png")
plt.close()

###############################
## Continous Values Plotting ##
###############################

plt.hist(df['study_hours_per_day'], bins='auto', align='mid', color='lightskyblue', edgecolor='black')
plt.title('Study hours ditribution of students')
plt.xlabel('Study hours per day')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.savefig("../../raw/hist_study.png")
plt.close()


plt.hist(df['social_media_hours'], bins='auto', align='mid', color='lightskyblue', edgecolor='black')
plt.title('Social media hours ditribution of students')
plt.xlabel('Social media hours per day')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.savefig("../../raw/hist_social.png")
plt.close()


plt.hist(df['netflix_hours'], bins='auto', align='mid', color='lightskyblue', edgecolor='black')
plt.title('Netflix hours ditribution of students')
plt.xlabel('Netflix hours per day')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.savefig("../../raw/hist_netflix.png")
plt.close()

plt.hist(df['attendance_percentage'], bins='auto', align='mid', color='lightskyblue', edgecolor='black')
plt.title('Attendance percentage ditribution of students')
plt.xlabel('Attendance percentage')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.savefig("../../raw/hist_attendance.png")
plt.close()

plt.hist(df['sleep_hours'], bins='auto', align='mid', color='lightskyblue', edgecolor='black')
plt.title('Sleep hours ditribution of students')
plt.xlabel('Sleep hours per day')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.savefig("../../raw/hist_sleep.png")
plt.close()

################################
## Categorial Values Plotting ##
################################