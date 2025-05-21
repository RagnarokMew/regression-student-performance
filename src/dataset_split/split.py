import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("../../data/noised_student_habits_performance.csv")

target = df['exam_score']

df = df.drop(columns=['exam_score', 'student_id'])

X_train, X_test, y_train, y_test = train_test_split(
    df, target, test_size=0.25, random_state=1984
)

print(f"Train size: {X_train.shape}")
print(f"Test size: {X_test.shape}")