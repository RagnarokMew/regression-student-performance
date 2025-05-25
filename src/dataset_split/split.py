import pandas as pd
from sklearn.model_selection import train_test_split

#####################
## Loading dataset ##
#####################

df = pd.read_csv("../../data/noised_student_habits_performance.csv")

#####################################
## Splitting dataset using sklearn ##
#####################################

target = df['exam_score']

df = df.drop(columns=['exam_score', 'student_id'])

X_train, X_test, y_train, y_test = train_test_split(
    df, target, test_size=0.25, random_state=1984
)

print(f"Train size: {X_train.shape}")
print(f"Train target size: {y_train.shape}")
print(f"Test size: {X_test.shape}")
print(f"Test target size: {y_test.shape}")

####################################
## Saving train and test datasets ##
####################################

X_train.to_csv("../../data/X_train.csv", index=False)
y_train.to_csv("../../data/y_train.csv", index=False)
X_test.to_csv("../../data/X_test.csv", index=False)
y_test.to_csv("../../data/y_test.csv", index=False)