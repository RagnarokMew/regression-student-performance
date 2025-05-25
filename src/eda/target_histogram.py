import sys
import pandas as pd
import matplotlib.pyplot as plt

csv_path = sys.argv[1]

df = pd.read_csv(csv_path)

plt.hist(df['exam_score'], bins='auto', align='mid', color='lightskyblue', edgecolor='black')
plt.title('Exam score ditribution of students')
plt.xlabel('Exam score')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.savefig("../../raw/hist_exam.png")
plt.close()